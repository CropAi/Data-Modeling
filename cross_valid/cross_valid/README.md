To install this module use the command "  pip install -e .  " in the root folder of module(by using cd command).

This module contains two functions
i)loading : It loads the h5 model into current program
ii)split_dataset_into_test_and_train_sets: It splits the dataset and makes folders on the basis of arguments provided , 
be sure provide correct arguments.

Wrapping it up


To include a module in your script, use from ... import. 
The keyword from locates the folder or file where the module is, the import keyword imports the file or
function/class you want to include. To include a module, it must be installed. Some modules comes already 
installed with Python, for all the others you need to use pip install. To create a plugin,
you need to create two folders with the same name. In the sub-folder, put your module and an 
empty init.py file. In the outer folder, create your setup.py file. To install a plugin locally,
and reflect any changes immediately, use pip install -e . utility.
