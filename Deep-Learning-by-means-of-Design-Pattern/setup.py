# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools import Extension
import numpy as np
import os

pyx_list = []
for dirpath, dirs, files in os.walk('.'):
    for f in files:
        if ".pyx" in f:
            pyx_list.append(os.path.join(dirpath, f))

setup(
    name='pydbm',
    version='1.0.1',
    description='pydbm is Python library for building restricted boltzmann machine, deep boltzmann machine, and multi-layer neural networks.',
    long_description='The models are functionally equivalent to stacked auto-encoder. The main function I observe is the same as dimensions reduction(or pre-training).',
    url='https://github.com/chimera0/accel-brain-code/tree/master/Deep-Learning-by-means-of-Design-Pattern',
    author='chimera0',
    author_email='ai-brain-lab@accel-brain.com',
    license='GPL2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
    ],
    keywords='restricted boltzmann machine autoencoder auto-encoder',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['numpy', 'cython', 'multipledispatch'],
    include_dirs=[ '.', np.get_include()],
    ext_modules=[
        Extension(
            "pydbm",
            pyx_list,
            include_dirs=[".", np.get_include()]
        )
    ]
)