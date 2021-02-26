from setuptools import setup

import os.path
# Change to the directory of this file before the build
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Build setup
setup(
    name='dicgan',
    version='1.0.0',
    packages=['dicgan'],
    license='MIT License',
    author='Cheng Ma',
    url='https://github.com/ananiask8/Deep-Iterative-Collaboration',
    description='Deep Face Super-Resolution with Iterative Collaboration '
                'between Attentive Recovery and Landmark Estimation',
    setup_requires=[
        'setuptools>=18.0'
    ],
    package_data={},
    install_requires=[],  # requirements.txt is included
    include_package_data=True,
)
