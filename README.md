# PyTestObject
A minimal example of using SIP to create a Python wrapper for a C++ library.

## Configuring and Compiling
The first step is run the following command:

	$ python configure.py

This will use SIP to generate the necessary C/C++ wrapper code and will create Makefile's for the library itself and the wrapper.

Now you can build and install the library

### *nix
    $ make
    $ make install

### win32 (mingw)
    c:\PyTestObject> mingw32-make

## Usage Example
	>>> from PyTestObject import TestObject
	>>> t=TestObject()
	TestObject!
