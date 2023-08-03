import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='OnePackLuck',
    version='0.1',
    authors='Marcelo Andrade, Marc Valduz',
    description='Paquete para el procesamiento de imágenes astronómicas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/marcelo-marchelini17/OnePackLuck',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'astropy',
        'Pillow'
        'tkinter',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
