import re
import numpy as np
import pandas as pd
import logging
from popopolus.utils import assign_populations
from popopolus.diversity_statistics.sfs import initialize_sfs

def estimate_wattersons(genotype_dat, tax_list, ind_map, intervals, output_dir):
    '''
    Returns a pandas DataFrame object of theta across each interval by population defined in the ind_map.

    Parameters:
        genotype_data (np.ndarray): a 2D numpy array of genotype data with shape (n_sites, n_individuals)
        tax_list (list): A list of individual names corresponding to the individual order of genotype_dat
        ind_map (dict): a dictionary mapping individuals in the VCF to a population or other identifier 
        intervals (list): a list of tuples defining the start and end positions of intervals to calculate theta over
        output_dir (string): the directory where all results will be written

    Returns:
        theta_df: a pandas DataFrame of theta values across each interval by population
    '''
    logging.info(f'Estimating Watterson Theta:\n')
    populations = assign_populations(ind_map)
    sfs = initialize_sfs(populations)
    # Only concern ourselves with the global calulcation for now. Will add per-interval later.
    for pop_index, pop in enumerate(populations.keys()):
        inds_in_pop = populations[pop]
        ind_indices = [tax_list.index(ind) for ind in inds_in_pop if ind in tax_list]
        logging.info(f'Calculating SFS for population: {pop} with {len(ind_indices)} individuals\n')
        pop_genotype_dat = genotype_dat[0, :, ind_indices]
        print(pop_genotype_dat.shape)
        #print(len(pop_genotype_dat[0,:]))
        #print(len(pop_genotype_dat[:,0]))
        #print(pop_genotype_dat)
        for site_index in range(len(pop_genotype_dat[0,:])):
            genotypes = pop_genotype_dat[: , site_index]
            # Quick fix for missing data but address weighting by variable sample size later
            genotypes[genotypes == -1] = 0
            # Count number of derived alleles (assuming 0, 1, 2 coding)
            n_derived = np.sum(genotypes)
            print(n_derived)
            sfs[pop_index, n_derived] += 1
    print(sfs)
    return(0)