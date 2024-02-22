# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:35:38 2024

@author: user
"""

#!pip install SimpleITK==1.2.0
#!pip install SimpleITK-SimpleElastix
#!pip install dicom2nifti
#install ANTsPY
#pip install antspynet

#import SimpleITK as sitk
import os
import zipfile
import shutil
import dicom2nifti
import ants
import numpy as np
import nibabel as nib
from PIL import Image
from antspynet.utilities import brain_extraction

def unzip_and_convert(Data_path):
    # unzipping files
    zip_file=[files for files in os.listdir(Data_path) if '.zip' in files][0]
    zipfile.ZipFile(os.path.join(Data_path,zip_file)).extractall(Data_path)
    subj_name=[subj for subj in os.listdir(Data_path) if '.zip' not in subj][0]
    os.remove(os.path.join(Data_path, zip_file))
    # convert dicom to nifti and remove dicom files
    dicom2nifti.convert_directory(os.path.join(Data_path, zip_file[:17]), Data_path, compression=False)
    shutil.rmtree(os.path.join(Data_path, zip_file[:17]))
    
    nifti_file=[nifti for nifti in os.listdir(Data_path) if (nifti.endswith('.nii')) and ('MNI' not in nifti)][0]

    return nifti_file, subj_name
                    
            
# registration
def registration_ANT(nifti_file, MNI_152, registered_T1_name, transform):
    if 'ANTsImage' not in str(type(nifti_file)):
        T1_nifti=ants.image_read(os.path.join(Data_path,nifti_file))
    else:
        T1_nifti=BCbrain
    MNI_nifti=ants.image_read(os.path.join(Data_path, MNI_152))
    
    transformation=ants.registration(fixed=MNI_nifti, moving=T1_nifti, type_of_transform=transform)
    registered_T1=transformation['warpedmovout']
    
    if registered_T1_name != None:
        registered_T1.to_file(os.path.join(Data_path, registered_T1_name))
        
    return registered_T1
    
              
    
# skull stripping and bias correction
def skull_stripping_with_biascorrection(reg_nifti, brain_mask_name):
    prob_brain_mask=brain_extraction(reg_nifti, modality='t1')
    brain_mask=ants.get_mask(prob_brain_mask, low_thresh=0.5)
    masked=ants.mask_image(reg_nifti, brain_mask)
    biascorrected_mask=ants.n4_bias_field_correction(masked)
    
    return biascorrected_mask
    
    



        
        

                    