[![License](https://img.shields.io/pypi/l/scipydirect.svg)](https://github.com/andim/scipydirect/blob/master/LICENSE)
[![Latest release](https://img.shields.io/pypi/v/scipydirect.svg)](https://pypi.python.org/pypi/scipydirect)
[![Py2.7/3.x](https://img.shields.io/pypi/pyversions/scipydirect.svg)](https://pypi.python.org/pypi/scipydirect)

![Status](https://img.shields.io/pypi/status/scipydirect.svg)
[![Build Status](https://travis-ci.org/andim/scipydirect.svg?branch=master)](https://travis-ci.org/andim/scipydirect)
[![Documentation Status](https://readthedocs.org/projects/scipydirect/badge/?version=latest)](https://scipydirect.readthedocs.io/en/latest/?badge=latest)

[![DOI](https://zenodo.org/badge/54575756.svg)](https://zenodo.org/badge/latestdoi/54575756)

# ScipyDIRECT: a Python wrapper of the DIRECT global optimization algorithm

DIRECT is a method to solve global bound constraint optimization problems and
was originally developed by D. R. Jones, C. D. Perttunen and B. E. Stuckmann.

ScipyDIRECT is a python wrapper around DIRECT. It enables using DIRECT from the
comfort of the Python scripting language.

The Scipydirect package uses the Fortran implementation of DIRECT written by Joerg M. Gablonsky, DIRECT Version 2.0.4. More information on the DIRECT
algorithm can be found in Gablonsky's [thesis](http://repository.lib.ncsu.edu/ir/bitstream/1840.16/3920/1/etd.pdf).

ScipyDIRECT is a fork of [pydirect](https://bitbucket.org/amitibo/pydirect). It provides an alternative interface to the DIRECT algorithm compatible with that used in `scipy.optimize`.

## Quick start

ScipyDIRECT is on [PyPI](https://pypi.python.org/pypi/scipydirect/) so you can install it using `pip install scipydirect`.

Then run the following minimal example.

```python
import numpy as np
from scipydirect import minimize

def obj(x):
    return (x**2).sum()

bounds = [[-3.0, 3.0], [0.5, 5.0]]
res = minimize(obj, bounds=bounds)
print(res)
```

## Documentation
You can access the documentation online at [Read the docs](http://scipydirect.readthedocs.io/en/latest/). If you install from source you can generate a local version by running `make html` from the `doc` directory.

## Support and contributing

For bug reports and enhancement requests use the [Github issue tool](http://github.com/andim/scipydirect/issues/new), or (even better!) open a [pull request](http://github.com/andim/scipydirect/pulls) with relevant changes. If you have any questions don't hesitate to contact me by email (andimscience@gmail.com) or Twitter ([@andimscience](http://twitter.com/andimscience)).

You can run the testsuite from the test directory: 

   cd test
   python test_direct.py
