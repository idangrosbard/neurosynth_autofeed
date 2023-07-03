import nibabel as nib
import nilearn
import nilearn.plotting as plotting
import matplotlib.pyplot as plt
from nilearn.input_data import NiftiLabelsMasker
from nilearn.datasets import fetch_icbm152_2009
import numpy as np

def create_voi_labels(voi_coords, data_shape):
    '''
    Create a temporary NIfTI image with VOI labels
    Input: x,y,z coordinates of the VOIs, shape of the image data
    Output: NIfTI image with labels
    '''

    labels = np.arange(len(voi_coords)) + 1  # Generate labels
    data = np.zeros(data_shape)  # Initialize data array

    for i, coord in enumerate(voi_coords):
        x, y, z = coord
        data[x, y, z] = labels[i]  # Set voxel at coordinates to label

    affine = np.eye(4)  # Create an identity affine matrix
    return nib.Nifti1Image(data, affine)

def plot_anatomical_voi(voi_coords):
    '''
    Plots the VOIs on the MNI template (anatomical scan)
    Input: x,y,z coordinates of the VOIs
    Output: plot of the MNI brain template with the VOI
    '''

    # Load MNI template from Nilearn datasets
    mni_template = fetch_icbm152_2009()
    mni_img = nib.load(mni_template['t1'])
    data_shape = mni_img.shape  # Get the shape of the image data

    # Create temporary NIfTI image with VOI labels
    labels_img = create_voi_labels(voi_coords, data_shape)

    masker = NiftiLabelsMasker(labels_img=labels_img, background_label=0,
                               detrend=True, standardize=True,
                               low_pass=None, high_pass=None, t_r=1,
                               memory='nilearn_cache', memory_level=1, verbose=0)

    # Apply the masker to create the VOI mask
    voi_mask = masker.fit_transform(mni_img)

    # Plot the MNI template
    display = plotting.plot_anat(mni_img, title='MNI Template', draw_cross=False,
                                 display_mode='ortho', annotate=False)

    # Add markers for the VOI
    for coord in voi_coords:
        display.add_markers([coord], marker_color='b', marker_size=100)

    plt.show()

if __name__ == '__main__':
    voi_coords = [[-45, 27, 36], [0, 0, 20], [34, 48, 0]]
    plot_anatomical_voi(voi_coords)
