# define "plot_anatomical_voi" function which accepts 3D numpy array of VOI coordinates and plots them on anatomical image

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from nilearn import plotting
# import MNI template
mni_template = nib.load('C:\\Users\\yohay\\Dropbox\\Yohay\\Studies\\MSc\\First_Year\\Semester_B\\Python_for_Neuroscience\\Assignments\\final\\MNI152_T1_2mm_brain.nii')

# define function
def plot_anatomical_voi(voi_coords):
    # create new figure
    fig = plt.figure()
    # plot anatomical image
    plotting.plot_anat(mni_template, title='Anatomical image', figure=fig)
    # plot VOI coordinates
    # plt.plot(voi_coords[:,0], voi_coords[:,1], voi_coords[:,2], 'ro')
    for coord in voi_coords:
        plt.plot(coord, 'ro')
    # plt.plot(voi_coords,'ro')
    # show figure
    plt.show()
    return fig

# test function
# define 7 VOI coordinates as numpy array
voi_coords = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60]])

# plot VOI coordinates on anatomical image
plot_anatomical_voi(voi_coords)
# show figure
plt.show()


# plot an anatomical image based on MNI template
# create new figure
fig = plt.figure()
# plot anatomical image
plotting.plot_anat(mni_template, title='Anatomical image', figure=fig)
# show figure
plt.show()

# the image contains 3 brain sections: sagittal, coronal and axial
# thus, when adding VOI coordinates, we need to add them in the following order:
# sagittal: x, y, z
# coronal: y, z, x
# axial: z, x, y

# plot VOI coordinates on anatomical image
# create new figure
fig = plt.figure()
# plot anatomical image
plotting.plot_anat(mni_template, title='Anatomical image', figure=fig)
# iterate though all the VOI coordinates
for coor in voi_coords:
    plt.plot(coor[:,0], coor[:,1], coor[:,2], 'ro')

# show figure
plt.show()


fig = plt.figure()
plotting.plot_anat(mni_template, title='Anatomical image', figure=fig)
plt.plot(voi_coords[5,:], 'ro')
plt.show()