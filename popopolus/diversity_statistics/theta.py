import re
import numpy as np
import pandas as pd
import logging

def estimate_wattersons(genotype_data, ind_map, intervals, output_dir):
    '''
    Returns a pandas DataFrame object of theta across each interval by population defined in the ind_map.

    Parameters:
        genotype_data (np.ndarray): a 2D numpy array of genotype data with shape (n_sites, n_individuals)
        ind_map (dict): a dictionary mapping individuals in the VCF to a population or other identifier 
        intervals (list): a list of tuples defining the start and end positions of intervals to calculate theta over
        output_dir (string): the directory where all results will be written

    Returns:
        theta_df: a pandas DataFrame of theta values across each interval by population
    '''

    