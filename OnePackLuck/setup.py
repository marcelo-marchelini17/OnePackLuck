from setuptools import setup, find_packages

setup(
    name='OnePackLuck',
    version='0.2',
    description='Procesamiento de imágenes FITS',
    author = 'Marcelo Andrade, Marc Valduz',
    url = 'https://github.com/marcelo-marchelini17/OnePackLuck',
    packages=find_packages(),
    install_requires=['numpy','matplotlib','astropy','Pillow']
)