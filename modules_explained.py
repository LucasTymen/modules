"""
https://www.codecademy.com/resources/docs/python/modules?page_ref=catalog

    Docs/
    Python/
    Modules

Modules

A module is a Python file that contains functions, definitions, and statements that can be included in other files
within an application. Technically, all files with the .py format are modules.

Conceptually, modules are named units of code that can be reused across applications and allows us to access shared
libraries (collections of modules) and packages (modules with nested modules and packages). Instead of entering commands
directly into a Python interpreter, code can be saved as a module for later use in other applications.
Creating and Importing Modules

A module can be created by saving a Python file with the .py file extension. It can then be imported into another .py
file with an import statement.

For example, a separate video_player.py file that was previously saved can be imported in other files:
"""
import video_player

# Rest of the program starts here...
"""
The program now has access to all functions, objects, and statements contained within the video_player module.
Importing Specific Resources

Instead of importing the whole module, individually named resources can be specified. For example:
"""
from video_player import VideoPlayer
"""
This will import only the VideoPlayer class from a given video_player module, rather than all types of collections
contained within it.

It’s often useful to import only what is needed to avoid slowing the program down and polluting the local namespace
where the code runs.
Namespaces and Scope

A module within our local namespace can be renamed by creating an alias using the as keyword. For example:
"""
from bs4 import BeautifulSoup as bs
"""
Aliasing is especially convenient for shortening module names and managing the local namespace where our code executes.

Once a module is imported, it is within the scope of the program and it can be accessed in the local namespace.
Python Standard Modules

Python comes with several different built-in modules that provide a variety of functions. They include:

    The collections module provides additional collection types.
    The functools module provides functions supporting a functional programming approach.
    The glob module allows matching file paths per Unix shell rules.
    The json module provides functions for dealing with JSON objects.
    The math module provides useful mathematical functions.
    The random module provides functions for dealing with random numbers.
    The time module provides various functions for dealing with time.

Python Third-Party Modules

Python has a very broad selection of third-party modules that are devoted to particular tasks.

These are third-party Python modules that have topic entries:

    NumPy: a popular open-source Python library used for complex mathematical operations and multi-dimensional arrays.
    Pandas: a popular open-source Python module used for data analysis and manipulation.

Below is a selection of other third-party modules of note:
Modules

PySpark
    A Python API for Apache Spark, consisting of several modules.
Pytorch
    An open-source framework that offers an optimized tensor library for deep learning.
tqdm
    A module that allows the generation of progress bars in Python.

Interested in helping build Docs? Read the Contribution Guide or share your thoughts in this feedback form.
Edit on GitHub

"""
