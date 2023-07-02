import nilearn.plotting as plotting
import matplotlib.pyplot as plt
from nilearn.input_data import NiftiSpheresMasker

def plot_associations(voi_coords_list, associated_regions_list, z_scores_list, radius=1):
    # Load the MNI152 template from Nilearn
    mni_template = plotting.find_parcellation('MNI152', space='mni152_2009', resolution_mm=1)

    # Loop through each VOI and plot the heat map
    for voi_coords, associated_regions, z_score in zip(voi_coords_list, associated_regions_list, z_scores_list):
        # Create the VOI mask
        masker = NiftiSpheresMasker(voi_coords, radius=radius, detrend=True, standardize=True)
        voi_mask = masker.fit_transform(mni_template)

        # Plot the MNI template
        display = plotting.plot_anat(mni_template, title='MNI Template', draw_cross=False,
                                     display_mode='ortho', annotate=False)

        # Overlay the VOI mask as a heatmap
        display.add_overlay(voi_mask, cmap='hot', vmin=0, vmax=1) 

        # Annotate the plot with the associated region and z-score
        annotation_text = f'Associated Region: {associated_regions}\nZ-score: {z_score:.2f}'
        display.annotate(annotation_text, (0.05, 0.95), xycoords='axes fraction',
                         color='white', fontsize=10, ha='left', va='top')

        return plt.show()