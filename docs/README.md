# <strong>Data Modelling for Crop Analyzer</strong>
Dataset used : https://www.kaggle.com/emmarex/plantdisease

## Tensorflow
Tensorflow is a popular end-to-end Machine Learning Library from Google whcih supports developing Machine Learning Models and Data Modelling. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.
![tensorflow](https://user-images.githubusercontent.com/43414928/76705997-45680400-670a-11ea-8493-7acc393ebcb8.png)

## Installation
-   For [Windows](https://github.com/CropAi/Data-Modeling/blob/master/docs/TensorFlowWindows.md)
-   For [Linux](https://github.com/CropAi/Data-Modeling/blob/master/docs/TensorFlowLinux.md)

# Our Modules
-   [label_binarizer_instance.py](https://github.com/CropAi/Data-Modeling/blob/master/modules/label_binarizer_instance.py)
-   [label_images.py](https://github.com/CropAi/Data-Modeling/blob/master/label_images.py)
  This python file is used to download the model file from google drive and run predictions on the image coming from the       frontend.  
  
   How to run label_images.py file for Backend
   You will need the encoder.pkl file present in Data Modelling Repo.
   Download this repo and extract it. Copy the encoder.pkl file and paste it in your backend devt. (encoder.pkl file is          experimental....Work in progress)

   Run the label_images.py file using this :.. `python3 label_images.py [path to your leaf image]`..

Refer [this](https://github.com/CropAi/Data-Modeling/blob/master/docs/transfer_learning.md) for knowing how to use transfer learning for Crop Disease Detection. 

Before contributing to this project do check [CONTRIBUTING.md](https://github.com/CropAi/Data-Modeling/blob/master/docs/CONTRIBUTING.md) file and [CODE_OF_CONDUCT.md](https://github.com/CropAi/Data-Modeling/blob/master/docs/CODE_OF_CONDUCT.md) file.

