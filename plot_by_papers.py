import nibabel as nib
import nilearn.plotting as plotting
import matplotlib.pyplot as plt
from nilearn.input_data import NiftiSpheresMasker
from nilearn.datasets import fetch_icbm152_2009
import plot_anatomical_voi

def choose_paper(papers_df, paper_name):
    '''
    a function that recives a paper name and returns the relevant VOIs 
    coordinates that are relavant for this paper
    '''
    coords = []
    for paper in papers_df['paper_name']: ##
        if paper == paper_name:
           coords.append(papers_df['coords'])

    return coords
    
def plot_by_papers(papers_df, paper_name):
    voi_coords = choose_paper(papers_df, paper_name)
    return plot_anatomical_voi(voi_coords)