# -*- coding: utf-8 -*-


class Distribution:
    
    def __init__(self, mu=0, sigma=1):
        """
        Generic distribution class for calculating and visualising 
        a probability distribution.
        
        Attributes:
            mean(float) representing the mean value of the distribution
            stdev(float) standard deviation
            data_list (list of floats) list of floats extracted from data file
        """
        
        self.mean = mu
        self.sigma = sigma
        self.data = []
        
    def read_data(self, filename):
        """
        Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        """
        with open(filename) as file:
            data_list = []
            line = file.readline()
            
            with line:
                data_list.append(int(line))
                line = file.readline()
                
            file.close()
            
            self.data = data_list