import numpy as np
class examdata:
    def __init__(self,csvfile):
        self.data=np.genfromtxt(csvfile,delimiter=',',skip_header=1,usecols=(1))
    def get_mean(self):
        return np.nanmean(self.data)
    def get_std(self):
        return np.nanstd(self.data)
    def fullrange(self):
        return np.nanmax(self.data)-np.nanmin(self.data)
    def percentiles(self):
        return np.nanpercentile(self.data,[25,75])
exam1=examdata("../data/exam.csv")
print(exam1.data)
print(exam1.get_mean())
print(exam1.get_std())
print(exam1.fullrange())
Q1,Q3=exam1.percentiles()
print("Q1:",Q1)
print("Q3:",Q3)