import matplotlib.pyplot as plt
class Pizza_graphic:
    def __init__(self,data_math,data_times):
        self.data = data
        upper_range = data_math["confidence_interval"] ["upper_range"]
        lower_range = data_math["confidence_interval"] ["lower_range"]

        mean = data_math["mean"]
        for time in data_times:
            if time < lower_range:
                c_lower_range += 1
            elif time >upper_range
                c_upper_range += 1
            else:
                C_confidence_interval += 1      
        labels = 'confidence_interval','up_confidence_interval','dow_confidence_interval'
        sizes = [c_lower_range,c_upper_range,C_confidence_interval]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startang=90  )
        ax1.axis('equal')
        plt.show()

data_times = 

       