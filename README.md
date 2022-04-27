# PythonX

Extension to the python language that allows for files with the .pyx extension to be compiled to python libraries to improve performance. Code in .pyx files is statically typed using python type hinting and can import to and from standard python files.

This is achieved by transpiling pyx files to boost python C++ files which are then compiled. MyPy is used to provide type checking. 