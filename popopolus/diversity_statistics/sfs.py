import re
import numpy as np
import pandas as pd
import logging

def initialize_sfs(populations):
    '''
    Initializes a site frequency spectrum (SFS) dictionary for each population.

    Parameters:
        populations (dict): a dict of unique populations as keys and individuals in those populations as a list as values
    Returns:
        sfs (ndarray): a numpy array of 1-d site frequency spectra for each population with shape (n_populations, max_sample_size + 1)
    '''
    n_populations = len(populations.keys())
    # Hardcoding all individuals as diploid for now
    ploidy_factor = 2
    max_sample_size = 0
    for pop in populations.keys():
        n_haplotypes = 0
        for ind in populations[pop]:
            n_haplotypes = n_haplotypes + ploidy_factor
            # In the future, we will access the ploidy by individual
        if n_haplotypes > max_sample_size:
            max_sample_size = n_haplotypes
    sfs = np.zeros((n_populations, max_sample_size + 1), dtype=np.uint32)
    return(sfs)