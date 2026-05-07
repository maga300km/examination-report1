import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class examdata:
    def __init__(self,csvfile):
        self.data=np.genfromtxt(csvfile,delimiter=',',skip_header=1,usecols=(1))
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
exam1=examdata("../data/exam.csv")
exam1.plots()