import statistics


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
