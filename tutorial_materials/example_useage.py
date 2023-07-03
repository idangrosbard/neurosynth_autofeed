import nibabel as nib
import numpy as np
import os
  
if __name__ == '__main__':

    # load an example file of analysis results stored in nifti format 
    file_name = r'.\tutorial_materials\accuracy_overlapISC_voxels_religious_secular_kosher.nii'

    # load the nifti file
    nifti_file = nib.load(os.path.join(file_name))

    # extract all values in voxel location coordinates
    nifti_data = nifti_file.get_fdata()

    # get the voxels location coordinates of all voxels with a value of 1
    voxels_coords = np.argwhere(nifti_data>0)

    # convert to MNI space using affine
    voxels_coords_MNI = nib.affines.apply_affine(nifti_file.affine, voxels_coords)
    print(voxels_coords_MNI)
    
    # as ints
    voxels_coords_MNI = np.round(voxels_coords_MNI).astype(int)


    # save voxels coordinates to a csv file, without decimal points
    np.savetxt(r'.\tutorial_materials\voxels_coords_MNI.csv', voxels_coords_MNI, delimiter=',', fmt='%i')


