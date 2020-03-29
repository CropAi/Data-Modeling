# Python script to download .h5 file from google drive.
import os

URL = 'https://drive.google.com/file/d/1PwifTMRZxzIbl-yDlR9cCVZrNxYg1JNd'
file_name = 'model.h5'
if not os.path.exists(file_name): # Check if file exists.
  print("Downloading weight file ...")
  !wget {URL} -O {file_name} # Use wget to download the file into current directory.
  print("Weight file downloaded!")
else:
  print("Weight file already downloaded!")
