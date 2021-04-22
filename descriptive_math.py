import statistics
import math

class descriptive_math:
    def __init__(self, times):
        self.times = list(times)

    def analysis(self):
        result = {}
        result["mean"] = self.mean()
        result["median"] = self.median()
        result["mode"] = self.mode()
        result["stddev"] = self.pstdev()
        result["varience"] = self.pvariance()
        result["max"] = self.time_max()
        result["min"] = self.time_min()
        result["amplitude"] = self.amplitude()
        result["confidence_interval"] = self.confidence_interval()
        return result

    def mean(self):
        return(statistics.mean(self.times))

    def median(self):
        return(statistics.median(self.times))

    def mode(self):
        return(statistics.mode(self.times))

    def multimode(self):
        return (statistics.multimode(self.times))

    def pstdev(self):
        return(statistics.pstdev(self.times, self.mean()))

    def pvariance(self):
        return(statistics.pvariance(self.times, self.mean()))

    def time_max(self):
        return(max(self.times))

    def time_min(self):
        return(min(self.times))

    def amplitude(self):
        return(self.time_max()-self.time_min())
    
    def confidence_interval(self):
        confidence_interval={}
        mean = self.mean() 
        Zc = 1.96
        standard_deviation = self.pstdev()
        population = len(self.times)
        margin_error = Zc*(standard_deviation/math.sqrt(population))
        upper_range = mean + margin_error
        lower_range = mean - margin_error
        confidence_interval["upper_range"] = upper_range
        confidence_interval["lower_range"] = lower_range
        confidence_interval["margin_error"] = margin_error
        return(confidence_interval)