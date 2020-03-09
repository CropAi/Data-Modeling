# <strong>Data Modelling for Crop Analyzer</strong>
Dataset used : https://www.kaggle.com/emmarex/plantdisease

## Installation

Tensorflow is a popular end-to-end Machine Learning Library from Google whcih supports developing Machine Learning Models and Data Modelling. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

![1_37N7BHNaEsXPaerNQ8wBdA](https://user-images.githubusercontent.com/43414928/76177685-07835100-61db-11ea-84d2-012d37783e0d.png)


### <strong>Tensorflow Installtion on Windows</strong>

#### Prerequisties
 To setup Tensorflow on Windows, you have to ensure that the necessary system requirements and prerequisties are followed: 
1. Python 3.5-3.7 should be installed on your System Path. You can check out your Python Version by opening the Command Prompt and typing in: ```python --version```
2. pip 19.0 or a higher version should be installed which enables to download Third Party Python Packages. You can check out your Python Version by opening the Command Prompt and typing in: ```pip --version```
3. Windows 7 or later (64-bit)
4. GPU Support with a CUDA-enabled Card

Once the necessary requirements and prerequisties have been verified, we will now move onto setting up Tensorflow on Windows by creating a Development Environment. For this purpose we are going to use **virtualenv** which is a tool to create isolated environments where we can install the necessary directories.

#### Installing a virtual environment
To install a Virtual Environment, follow the following steps: 
1. Open the Command Prompt.
2. Go to the C:\ directory in the Command Prompt. 
3. Type the Command: ```pip3 install -U pip virtualenv```
4. Check if Virtual Environment has been setup or not by running the following command: ```virtualenv --version```

Since we have installed a Virtual Environment, we will now try to set up a Virtual Environment where we can install Tensorflow: 
1. We will first create a Virtual Environment by making a ```./venv``` directory: 
```virtualenv --system-site-packages -p python3 ./venv```
2. Now we will activate the Virtual Environment: 
```.\venv\Scripts\activate```
3. Now we will see what are the list of packages that have already been installed using pip: 
```pip list```
4. Incase the pip version has been depercated, it is advisable to follow these steps to upgrade the pip: 
```pip install --upgrade pip```
5. To install Tensorflow, now type in the command: 
```pip install tensorflow```
6. In case you want to exit the virtual environment you can just type in the command: 
```deactivate```

These commands will install Tensorflow on a Windows System with ease using pip. In case you are using an Anaconda Navigator, there are seperate set of commands which are explained here: 

1. Open Command Prompt and type in the command:
```conda info```
This command will display all of the necessary details of Anaconda including the Active Environments and more.
2. Create an Environment on Conda using the following command: 
```conda create -n [environment-name]```
Let's say I want to name my environment as "TensorTest" so my command would be: 
```conda create -n tensortest```
3. Now we will activate the command that we have just created: 
```activate tensortest```
4. Now run the following environment that you have just created: 
```conda install tensorflow```

Now we have seen how we can install Tensorflow on Windows using pip and conda. Now let's verify that we have installed Tensorflow successfully by running a simple Tensorflow Code: 
1. Open the Command Prompt. 
2. Type the following command to kickstart a Python Shell: ```python```
3. Now type the following code: 
```python
>>> import tensorflow as tf
>>> output=tf.constant("Hello World")
>>> sess=tf.Session()
>>> print(sess.run(output))
'Hello World'
>>> sess.close()
```

We will see an output on the Command Prompt Screen which will verify that Tensorflow is now up and running on our system.


<hr />


### <strong>Tensorflow Installtion on Linux</strong>

### <b>Prerequisites</b>
1. Python 3.3 or higher
2. At least 1GB of RAM

### <b>Step 1: Install python3-venv</b>
```
apt-get install python3-venv -y
```

### <b>Step 2: Create and activate a Python virtual environment</b>
```
python3 -m venv venv
source ./venv/bin/activate
```
output:
```
(venv) root@ubuntu:~#
```

### <b>Step 3: Update PIP</b>
```
pip install -U pip
```

### <b>Step 4: Update setuptools</b>
```
pip install -U setuptools
```

### <b>Step 5: Install TensorFlow</b>
```
pip install tensorflow
```

> #### *Refer the official tensorflow documentation for further details :* https://www.tensorflow.org/install
