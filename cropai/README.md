Wrapping it up

Now you know everything you need to be productive with Python modules. You know how to import them, how they are structured and how to create your own. With this knowledge you will be developing big and scalable applications before you know it. Here we have the key elements you must remember.

To include a module in your script, use from ... import. The keyword from locates the folder or file
where the module is, the import keyword imports the file or function/class you want to include.
To include a module, it must be installed. Some modules comes already installed with Python, for all 
the others you need to use pip install.
To create a plugin, you need to create two folders with the same name. In the sub-folder, put your 
module and an empty __init__.py file. In the outer folder, create your setup.py file.
To install a plugin locally, and reflect any changes immediately, use pip install -e . utility.
