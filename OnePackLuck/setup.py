from setuptools import setup, find_packages

setup(
    name='imagen_processing',
    version='0.1',
    description='Procesamiento de imágenes FITS',
    author = 'MArcelo Andrade, Marc Valduz'
    url = 'https://github.com/marcelo-marchelini17/OnePackLuck',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'astropy',
        'Pillow'
    ],
)
