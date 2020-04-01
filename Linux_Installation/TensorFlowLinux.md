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

