import random
import numpy

class MonteCaro:

    def __init__(self, mean, std_dev, sample_size):
        self.mean = mean
        self.std_dev = std_dev
        self.sample_size = sample_size
        self.distribution = self._initialize()

    def get_percentile(self, input):
        return self.distribution[int(input/100 * self.sample_size) ]

    def _initialize(self):
        dist = numpy.random.normal(self.mean, self.std_dev, self.sample_size)
        sorted_distribution = sorted(dist)
        return sorted_distribution


class FutureValueAnalysis:

    def __init__(self, inflation_rate, period, present_value):
        self.period = period
        self.inflation_rate = inflation_rate
        self.present_value = present_value

    def future_value(self, nominal_rate):
        real_rate = self._calc_real_rate(nominal_rate, self.inflation_rate)
        fv = self.present_value
        for i in range(self.period):
            fv = fv + fv * real_rate
        return fv

    # Calculate inflation adjusted rate
    def _calc_real_rate(self, nominal_rate, inflation_rate):
        return ((1 + nominal_rate) / (1 + inflation_rate)) - 1


if __name__ == '__main__':

    inflation_rate = 0.035
    present_value = 100000
    period = 20

    mc = MonteCaro(9.4324, 15.675,10000)

    worst_10 = mc.get_percentile(10)
    best_10 = mc.get_percentile(90)
    median = mc.get_percentile(50)

    f = FutureValueAnalysis(inflation_rate, period, present_value)
    print("*** Aggressive approach - Inflation adjusted ***")
    print("Worst Case - ", f.future_value(worst_10/100))
    print("Best Case - ", f.future_value(best_10/100))
    print("Median - ",f.future_value(median/100))

    print ("\n")
    mc = MonteCaro(6.189,6.3438,10000)
    worst_10 = mc.get_percentile(10)
    best_10 = mc.get_percentile(90)
    median = mc.get_percentile(50)

    print("*** Very Conservative approach - Inflation adjusted *** ")
    print("Worst Case - ", f.future_value(worst_10 / 100))
    print("Best Case - ", f.future_value(best_10 / 100))
    print("Median - ", f.future_value(median / 100))


