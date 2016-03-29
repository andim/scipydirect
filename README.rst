.. image:: https://readthedocs.org/projects/scipydirect/badge/?version=latest
    :target: http://scipydirect.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

===================
Scipydirect
===================

DIRECT is a method to solve global bound constraint optimization problems and
was originally developed by D. R. Jones, C. D. Perttunen and B. E. Stuckmann.

`scipydirect` is a python wrapper around DIRECT. It enables using DIRECT from the
comfort of the Python scripting language.

The `scipydirect` package uses the Fortran implementation of DIRECT written by Joerg M. Gablonsky, DIRECT Version 2.0.4. More information on the DIRECT
algorithm can be found in Gablonsky's
`thesis <http://repository.lib.ncsu.edu/ir/bitstream/1840.16/3920/1/etd.pdf>`_.

`scipydirect` is a fork of `pydirect <https://bitbucket.org/amitibo/pydirect>`_.
It provides an alternative interface to the DIRECT algorithm compatible with that used in `scipy.optimize`.

Installing
==========

Use ``setup.py``::

   python setup.py install


Reading the docs
================

After installing::

   cd doc
   make html

Then, direct your browser to ``build/html/index.html``.


Testing
=======

To run the tests with the interpreter available as ``python``, use::

   cd test
   python test_direct.py


Conditions for use
==================

`scipydirect` is open-source code released under the `MIT <http://opensource.org/licenses/MIT>`_ License.


Contributing
============

For bug reports use the Github issue tool.
You can also send wishes, comments, patches, etc. to andisspam@gmail.com
