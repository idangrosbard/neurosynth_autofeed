import nibabel as nib
import nilearn.plotting as plotting
import matplotlib.pyplot as plt
from nilearn.input_data import NiftiSpheresMasker
from nilearn.datasets import fetch_icbm152_2009
import plot_anatomical_voi

def choose_assosiations(assosiations_df, assosiations_name):
    '''
    a function that recives a association/function name and returns the relevant VOIs 
    coordinates that are relavant for this association/function.
    '''
    coords = []
    for asso in assosiations_df['assosiations_name']: 
        if asso == assosiations_name:
           coords.append(assosiations_df['coords'])

    return coords
    
def plot_by_assosiations(assosiations_df, assosiations_name):
    voi_coords = choose_assosiations(assosiations_df, assosiations_name)
    return plot_anatomical_voi(voi_coords)