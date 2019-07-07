import numpy as np

f = open('data_stats.txt', 'r')
data_for_calculation = [int(line) for line in f]
f.close()

class CalculateStats:
    def __init__(self, data_for_calculation):
        self.data_for_calculation = data_for_calculation

    def percentile(self):
        data = np.array(self.data_for_calculation)
        percentile = np.percentile(data, 90)
        return percentile

    def median(self):
        data_sort = sorted(self.data_for_calculation)
        len_data = len(data_sort)
        index_mid = (len_data - 1) // 2
        if index_mid % 2:
            return data_sort[index_mid]
        else:
            return (data_sort[index_mid] + data_sort[index_mid + 1]) / 2.0

    def average(self):
        data = sum(self.data_for_calculation)
        return data / len(self.data_for_calculation)

    def maximum(self):
        return max(self.data_for_calculation)

    def minimum(self):
        return min(self.data_for_calculation)


if __name__ == '__main__':
    calc = CalculateStats(data_for_calculation)
    print('-----------------------------------------------')
    print("90 percentile <{}>".format(calc.percentile()))
    print("median <{}>".format(calc.median()))
    print("average <{}>".format(calc.average()))
    print("max <{}>".format(calc.maximum()))
    print("min <{}>".format(calc.minimum()))
    print('-----------------------------------------------')