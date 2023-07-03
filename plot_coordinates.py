from nilearn import plotting
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from nilearn import datasets

def plot_anatomical_voi(voi_coords):
    # Load the MNI template
    template_img = datasets.load_mni152_template()

    # Load the MNI template
    # template_img = nib.load(mni_template_path)
    template_data = template_img.get_fdata()
    affine = template_img.affine
    # Set all values in the template to 0
    template_data[:] = 0

    # convert numpy array to a list
    voi_coords = voi_coords.tolist()
    # Add the coordinates to the template
    for coord in voi_coords:
        # Transform MNI coordinates to voxel coordinates
        voxel_coord = nib.affines.apply_affine(np.linalg.inv(affine), coord)

        # Convert voxel coordinates to integer indices
        voxel_indices = np.round(voxel_coord).astype(int)

        # Set the corresponding voxel in the template to 1
        template_data[tuple(voxel_indices)] = 0.5

    # Convert the template data to a Nifti image
    coords_img = nib.Nifti1Image(template_data, affine=affine, header=template_img.header)

    # Plot the coordinates on an MNI template
    brain_figure = plotting.plot_glass_brain(
        stat_map_img=coords_img,
        threshold=None,
        colorbar=False,
        plot_abs=False,
        symmetric_cbar=False,
        vmax=1,
        vmin=None,
        black_bg=False,
        title='Coordinates on MNI template',
        display_mode='ortho',
        figure=None,
        axes=None,
        annotate=True,
        output_file=None,
    )

    return brain_figure