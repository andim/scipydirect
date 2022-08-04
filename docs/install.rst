.. highlight:: sh

Installation
============

The quickest way to install is to type::

    $ pip install scipydirect

More detailed instructions follow. To install scipydirect you will need the following prerequisites:

* python 2.7 or 3.x
* a FORTRAN compiler
* numpy
* matplotlib (for the examples)

The `Anaconda <http://www.anaconda.com/download/>`_ distribution is a great way to install these 
dependencies.

Download the source files of scipydirect, unzip, and then execute::

    $ python setup.py install

You can test the installation by running the examples under the folder ``test/``.

If you're running into trouble when reinstalling scipydirect in different virtual environments make sure to use `--no-cache-dir` with `pip` as otherwise the Fortran extension might not be compiled properly.
