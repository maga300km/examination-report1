import numpy as np
import pandas as pd
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
exam1=examdata("../data/exam.csv")
print(exam1.get_group_info())
exam1.save_info()
