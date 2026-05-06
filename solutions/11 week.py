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
exam1=examdata("../data/exam.csv")
print(exam1.df)
print(exam1.get_describe())
print("Бағасы қойылмаған группалар:",exam1.not_graded())
