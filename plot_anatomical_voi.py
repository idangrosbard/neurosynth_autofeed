import nibabel as nib
import nilearn.plotting as plotting
import matplotlib.pyplot as plt
from nilearn.input_data import NiftiSpheresMasker
from nilearn.datasets import fetch_icbm152_2009

def plot_anatomical_voi(list(voi_coords)):

    '''
    Plots the VOIs on the MNI template (anatomical scan)
    Input: x,y,z coordinates of the VOIs
    Output: plot of the MNI brain template with the VOI
    '''

    # Load MNI template from Nilearn datasets
    mni_template = fetch_icbm152_2009()
    mni_img = nib.load(mni_template['t1'])

    # Define the sphere radius for the VOI (in mm)
    sphere_radius = 1  

    masker = NiftiSpheresMasker(voi_coords, radius=sphere_radius,
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
        display.add_markers(coord, marker_color='b', marker_size=100)

    return plt.show()

if __name__ == '__main__':
    voi_coords = [[-45, 27, 36], [0, 30, 20], [-6, 48, -18]]
    plot_anatomical_voi(voi_coords) 