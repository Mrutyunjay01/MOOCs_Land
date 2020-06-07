import math
import matplotlib.pyplot as plt


class Gaussian:
    """
    Gaussian distribution class for calculating and visualizing
    a gaussian distribution.

    Attributes:
        mean (float) : representing the mean value of the distribution
        stdev (float) : representing the standard deviation of the distribution
        data_list (list of floats) : a list of float values from the data file
    """

    def __init__(self, mu=0, sigma=1):

        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        """
        Function to calculate the mean of the data
        :return: float : mean of the data
        """
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Function to calculate the standard deviation of the data
        :param sample: (bool) whether the data represents a sample or population
        :return: (float) standard deviation of the data
        """

        if sample:
            n = len(self.data) - 1

        else:
            n = len(self.data)

        mean = self.mean
        sigma = 0
        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)
        self.stdev = sigma

        return self.stdev

    def read_data_file(self, file_name, sample=True):
        """
        Function to read in data from a text file. The txt file should have one number(float) per line. The numbers are
        stored in the data attribute. After reading in the file, the mean and standard deviation are calculated.

        :param file_name: (string) name of the file
        :param sample: (bool)
        :return:  None
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()

            while line:
                data_list.append(int(line))
                line = file.readline()

        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

        pass

    def plot_histogram(self):
        """
        Function to output a histogram of the instance variable data using matplotlib.pyplot lib
        :return:
        """

        plt.hist(self.data)
        plt.title('Histogram of data')
        plt.xlabel('Data')
        plt.ylabel('Count')

    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution.
        :param x: point for calculating the probability density function
        :return: pdf output
        """

        return (1. / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)
        pass

    def plot_pdf(self, n_spaces=50):
        """
        Function to plot the normalized histogram of the data and a plot of the probability density function along the
        same range.
        :param n_spaces: Number of data points
        :return: list : x, y values for pdf plot
        """

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculate the interval between the x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal distribution for \n sample Mean and Sample standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
