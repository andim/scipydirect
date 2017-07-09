import setuptools


DISTNAME            = "scipydirect"
DESCRIPTION         = "Python wrapper to the DIRECT algorithm"
LONG_DESCRIPTION    ="""
DIRECT is a method to solve global bound constraint optimization problems and
was originally developed by D. R. Jones, C. D. Perttunen and B. E. Stuckmann.

The scipydirect is a fork of pydirect providing a scipy.optimize compatible
syntax. It uses the Fortan implementation of DIRECT written by
Joerg M Gablonsky, DIRECT Version 2.0.4.

For more info see the `documentation <http://scipydirect.readthedocs.io/en/latest/>`_ or the `source code <http://github.com/andim/scipydirect>`_.
"""
MAINTAINER          = "Andreas Mayer"
MAINTAINER_EMAIL    = "andimscience@gmail.com"
URL                 = "http://github.com/andim/scipydirect"
LICENSE             = "MIT"
VERSION             = "1.2"

classifiers =  ['Development Status :: 5 - Production/Stable',
                'Programming Language :: Python',
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 2.7",              
                "Programming Language :: Python :: 3",              
                "Programming Language :: Python :: 3.5",              
                "Programming Language :: Python :: 3.6",              
                'License :: OSI Approved :: MIT License',
                'Intended Audience :: Science/Research',
                'Topic :: Scientific/Engineering',
                'Topic :: Scientific/Engineering :: Mathematics',
                'Operating System :: OS Independent']

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(DISTNAME, parent_package, top_path,
                           version=VERSION,
                           maintainer=MAINTAINER,
                           maintainer_email=MAINTAINER_EMAIL,
                           description=DESCRIPTION,
                           license=LICENSE,
                           url=URL,
                           long_description=LONG_DESCRIPTION)

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup
    kwargs = dict( 
            packages=setuptools.find_packages(),
            include_package_data=True,
            platforms=["any"],
            requires=["numpy"],
            install_requires=["numpy"],
            tests_require=['nose',],
            test_suite='nose.collector',
            zip_safe=True,
            classifiers=classifiers,
            )
    try:
        thiskwargs = kwargs.copy()
        config = configuration()
        config.add_extension('direct', sources=['src/direct.pyf', 'src/DIRect.f', 'src/DIRserial.f', 'src/DIRsubrout.f'])
        thiskwargs.update(config.todict())
        setup(**thiskwargs)
    except:
        # if there was an error try building module without Fortran extension
        # the module will not be usable, but documentation can be built
        # (for readthedocs)
        thiskwargs = kwargs.copy()
        config = configuration()
        thiskwargs.update(config.todict())
        setup(**thiskwargs)
