from setuptools import setup, find_packages

setup(
    name='imagen_processing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'astropy',
        'Pillow'
    ],
)