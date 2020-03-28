# <strong>Data Modelling for Crop Analyzer</strong>
Dataset used : https://www.kaggle.com/emmarex/plantdisease

## Installation
Tensorflow is a popular end-to-end Machine Learning Library from Google whcih supports developing Machine Learning Models and Data Modelling. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.
![tensorflow](https://user-images.githubusercontent.com/43414928/76705997-45680400-670a-11ea-8493-7acc393ebcb8.png)



## <strong>Tensorflow Installation on Windows</strong>

#### <b>Prerequisites</b>
1. Python 3.5-3.7 should be installed on your System Path. Check out your Python Version by opening the Command Prompt and typing in:     ```python --version```
2. pip 19.0 or a higher version should be installed which enables to download Third Party Python Packages. Check out your Python Version by opening the Command Prompt and typing in:
    ```pip --version```
3. Windows 7 or later (64-bit)
4. GPU Support with a CUDA-enabled Card

Once the necessary requirements and prerequisites have been verified, we will now move onto setting up Tensorflow on Windows by creating a Development Environment. For this purpose we are going to use **virtualenv** which is a tool to create isolated environments where we can install the necessary directories.

#### Installing a virtual environment
To install a Virtual Environment, follow the following steps: 
#### <b>Step 1: Open the Command Prompt.</b>
```
apt-get install python3-venv -y
```
#### <b>Step 2: Go to the C:\ directory in the Command Prompt</b>
#### <b>Step 3:Type the Command:</b>
```
pip3 install -U pip virtualenv
```
#### <b>Step 4:Check if Virtual Environment has been setup or not by running the following command:</b>
```
virtualenv --version
```

Since we have installed a Virtual Environment, we will now try to set up a Virtual Environment where we can install Tensorflow: 
#### <b>Step 1: Create a Virtual Environment by making a ```./venv``` directory:</b>
```
virtualenv --system-site-packages -p python3 ./venv
```
#### <b>Step 2: Activate the Virtual Environment:</b>
```
.\venv\Scripts\activate
```
#### <b>Step 3:Now we will see what are the list of packages that have already been installed using pip: </b>
```
pip list
```
#### <b>Step 4:Incase the pip version has been deprecated, it is advisable to follow these steps to upgrade the pip:</b>
```
pip install --upgrade pip
```
#### <b>Step 5:To install Tensorflow </b>
```
pip install tensorflow
```
#### <b>Step 6:In case you want to exit the virtual environment just type in the command:</b>
```
deactivate
```


These commands will install Tensorflow on a Windows System with ease using pip. In case you are using an **Anaconda Navigator**, there are a separate set of commands which are explained here: 

#### <b>Step 1: Open the Command Prompt and type in the command:</b>
```
conda info
```
This command will display all of the necessary details of Anaconda including the Active Environments and more
#### <b>Step 2: Create an Environment on Conda using the following command:</b>
```
conda info
```
#### <b>Step 3:Type the Command:</b>
```
conda create -n [environment-name]
```
Let's say I want to name my environment as "TensorTest" so my command would be: 
```conda create -n tensortest```
#### <b>Step 4:Now run the following environment that you have just created:</b>
```
conda install tensorflow
```

Now we have seen how we can install Tensorflow on Windows using pip and conda. Now let's verify that we have installed Tensorflow successfully by running a simple Tensorflow Code: 
#### <b>Step 1: Open the Command Prompt.</b>
#### <b>Step 2: Type the following command to kickstart a Python Shell:</b>
```
python
```
#### <b>Step 3: Now type the following code:</b>
```
python
>>> import tensorflow as tf
>>> output=tf.constant("Hello World")
>>> sess=tf.Session()
>>> print(sess.run(output))
'Hello World'
>>> sess.close()
```
We will see an output on the Command Prompt Screen which will verify that Tensorflow is now up and running on our system.





## <strong>Tensorflow Installation on Linux</strong>

### <b>Prerequisites</b>
1. Python 3.3 or higher
2. pip 19.0 or a higher version 
3. At least 1GB of RAM

### Installation
#### <b>Step 1: Install python3-venv</b>
```
apt-get install python3-venv -y
```

#### <b>Step 2: Create and activate a Python virtual environment</b>
```
python3 -m venv venv
source ./venv/bin/activate
```
output:
```
(venv) root@ubuntu:~#
```

#### <b>Step 3: Update PIP</b>
```
pip install -U pip
```

#### <b>Step 4: Update setuptools</b>
```
pip install -U setuptools
```

#### <b>Step 5: Install TensorFlow</b>
```
pip install tensorflow
```

*For more details, visit the official tensorflow documentation page : https://www.tensorflow.org/*

Before contributing to this project do check [CONTRIBUTING.md](https://github.com/CropAi/Data-Modeling/blob/master/CONTRIBUTING.md) file.

