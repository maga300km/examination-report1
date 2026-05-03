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
exam1=examdata("../data/exam.csv")
print(exam1.data)
print(exam1.get_mean())
print(exam1.get_std())
print(exam1.fullrange())



