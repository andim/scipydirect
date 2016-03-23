import setuptools


DISTNAME            = "scipydirect"
DESCRIPTION         = "Python wrapper to the DIRECT algorithm"
LONG_DESCRIPTION    ="""
DIRECT is a method to solve global bound constraint optimization problems and
was originally developed by D. R. Jones, C. D. Perttunen and B. E. Stuckmann.

The scipydirect package uses the fortan implementation of DIRECT written by
Joerg M Gablonsky, DIRECT Version 2.0.4.

Its call syntax is compatible with the optimizer's from scipy.optimize
"""
MAINTAINER          = "Andreas Mayer"
MAINTAINER_EMAIL    = "andisspam@gmail.com"
URL                 = "http://github.com/andim/scipydirect"
LICENSE             = "MIT"
VERSION             = "1.0"

classifiers =  ['Development Status :: 5 - Production/Stable',
                'Programming Language :: Python',
                'License :: OSI Approved :: MIT License',
                'Intended Audience :: Science/Research',
                'Topic :: Scientific/Engineering',
                'Topic :: Scientific/Engineering :: Mathematics',
                'Operating System :: OS Independent']

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(DISTNAME, parent_package, top_path,
                           version=VERSION,
                           maintainer=MAINTAINER,
                           maintainer_email=MAINTAINER_EMAIL,
                           description=DESCRIPTION,
                           license=LICENSE,
                           url=URL,
                           long_description=LONG_DESCRIPTION)

    config.add_extension('direct', sources=['src/direct.pyf', 'src/DIRect.f', 'src/DIRserial.f', 'src/DIRsubrout.f'])

    return config


if __name__ == "__main__":

    from numpy.distutils.core import setup
    setup(configuration=configuration,
        packages=setuptools.find_packages(),
        include_package_data=True,
        platforms=["any"],
        requires=["numpy"],
        tests_require=['nose',],
        test_suite='nose.collector',
        zip_safe=True,
        classifiers=classifiers)
