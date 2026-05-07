import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
import io
class examdata:
    def __init__(self,csvfile):
        self.data=np.genfromtxt(csvfile,delimiter=',',skip_header=1,usecols=(1))
        try:
            csvfile.seek(0)
        except AttributeError:
            pass
        self.df=pd.read_csv(csvfile)
    def get_mean(self):
        return np.nanmean(self.data)
    def get_std(self):
        return np.nanstd(self.data)
    def fullrange(self):
        return np.nanmax(self.data)-np.nanmin(self.data)
    def percentiles(self):
        return np.nanpercentile(self.data,[25,75])
    def get_describe(self):
        return self.df.describe()
    def not_graded(self):
        return self.df['score'].isnull().sum()
    def get_dtypes(self):
        return self.df.dtypes
    def get_group_info(self):
        group_mean=self.df.groupby('group')['score'].mean()
        group_count=self.df.groupby('group').size()
        summary=pd.concat([group_mean,group_count],axis=1).reset_index()
        summary.columns = ['group', 'mean_score', 'number_of_students']
        return summary
    def save_info(self):
        summary=self.get_group_info()
        summary.to_csv('../output/summary_groups.csv',index=False)
    def plots(self):
        clean_data=self.data[(~np.isnan(self.data))]
        plt.figure(figsize=(10,8))
        plt.hist(clean_data,bins=10,edgecolor='black',color='red')
        plt.xlabel('Score')
        plt.ylabel('Number of students')
        plt.savefig("../output/scorehistogram.png")
        plt.close()
        summary=self.get_group_info()
        plt.figure(figsize=(10, 8))
        plt.bar(summary["group"].astype(str),summary["mean_score"],color="green")
        plt.xlabel('Group')
        plt.ylabel('Mean Score')
        plt.savefig("../output/groupmeanbar.png")
        plt.close()

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['file']

    content = io.StringIO(
        file.stream.read().decode('utf-8')
    )

    exam = examdata(content)

    global_mean = exam.get_mean()

    group_info = exam.get_group_info()

    group_dict = dict(zip(
        group_info['group'].astype(str),
        group_info['mean_score'].round(2)
    ))

    return jsonify({
        'global_mean': round(float(global_mean), 2),
        'group_means': group_dict
    })


if __name__ == '__main__':
    app.run(debug=True)
#curl.exe -X POST -F "file=@data/exam.csv" http://127.0.0.1:5000/analyze