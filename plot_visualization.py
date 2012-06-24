""" Simple example to show data manipulation and visualization.
"""

# Fetch data ################################################################
from nisl import datasets
haxby = datasets.fetch_haxby()

# Get the files relative to this dataset
files = haxby.files
bold = files[1]

# Load the NIfTI data
import nibabel
data = nibabel.load(bold).get_data()

# Visualization #############################################################
import numpy as np
import pylab as pl
pl.figure()
pl.subplot(131)
pl.axis('off')
pl.title('Coronal')
pl.imshow(np.rot90(data[:, 32, :, 100]), interpolation='nearest',
          cmap=pl.cm.gray)

pl.subplot(132)
pl.axis('off')
pl.title('Sagittal')
pl.imshow(np.rot90(data[15, :, :, 100]), interpolation='nearest',
          cmap=pl.cm.gray)

pl.subplot(133)
pl.axis('off')
pl.title('Axial')
pl.imshow(np.rot90(data[:, :, 32, 100]), interpolation='nearest',
          cmap=pl.cm.gray)

# Extracting a brain mask ###################################################

# Simple computation of a mask from the fMRI data
from nisl.masking import compute_mask
mask = compute_mask(data)

# We create a new figure
pl.figure()
# A plot the axial view of the mask to compare with the axial
# view of the raw data displayed previously
pl.imshow(np.rot90(mask[:, :, 32]), interpolation='nearest')
pl.show()

# Applying the mask #########################################################

masked_data = data[mask]


