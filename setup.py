"""Based on: https://github.com/pypa/sampleproject."""

import os
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


tests_require = ['flake8', 'mock', 'pytest', 'pytest-flake8', 'pytest-cov']

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        if 'doc' in path or 'www' in path:
            continue
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

setuptools.setup(
    name="thr3d-exrsplit",
    version='0.0.1',
    author="sgsco|THR3D",
    author_email="support@thr3dcgi.com",
    description="Split/merge multi-layer exr images tool for the THR3D CGI pipeline.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tiagoshibata/exrsplit',
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires=['OpenEXR'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={'test': tests_require},

    setup_requires=['pytest-runner'],

    tests_require=tests_require,

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},
)
