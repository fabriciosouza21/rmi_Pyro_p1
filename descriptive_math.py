import statistics
from scipy.stats import skew
class descriptive_math:
    def __init__(self,times):
        self.times = list(times)
    def mean(self):
        return(statistics.fmean(self.times))
    def  median(self):
        return(statistics.median(self.times))

    def mode(self):
        return(statistics.mode(self.times))
    def multimode(self):
        return (statistics.multimode(self.times))
    def pstdev(self):
        return(statistics.pstdev(self.times,self.mean()))
    def pvariance(self):
        return(statistics.pvariance(self.times,self.mean()))
    def time_max(self):
        return(max(self.times))
    def time_min(self):
        return(min(self.times))
    def amplitude(self):
        return(self.time_max()-self.time_min())

    
