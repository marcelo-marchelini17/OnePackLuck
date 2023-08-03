# Softwareproject
import numpy as np
from astropy.io import fits
from astropy.visualization import ZScaleInterval
from astropy.stats import sigma_clipped_stats
from scipy.ndimage import median_filter, gaussian_filter
import matplotlib.pyplot as plt

def load_fits_image(file_path):
    """
    Carga una imagen FITS desde un archivo y devuelve un objeto de imagen.
    """
    hdulist = fits.open(file_path)
    image = hdulist[0].data
    hdulist.close()
    return image

def save_fits_image(image, file_path):
    """
    Guarda una imagen FITS en un archivo.
    """
    hdu = fits.PrimaryHDU(image)
    hdulist = fits.HDUList([hdu])
    hdulist.writeto(file_path, overwrite=True)

def display_image(image):
    """
    Muestra una imagen utilizando matplotlib.
    """
    plt.imshow(image, cmap='gray')
    plt.colorbar()
    plt.show()

def rescale_image(image, scale_range=(0, 1)):
    """
    Reescala una imagen en un rango específico.
    """
    min_val, max_val = scale_range
    scaled_image = (image - np.min(image)) / (np.max(image) - np.min(image))
    scaled_image = scaled_image * (max_val - min_val) + min_val
    return scaled_image

def stretch_image(image, stretch='linear', **kwargs):
    """
    Estira la escala de una imagen para mejorar el contraste visual.
    """
    interval = ZScaleInterval(**kwargs)
    vmin, vmax = interval.get_limits(image)
    stretched_image = interval(image)
    return stretched_image

def apply_median_filter(image, size):
    """
    Aplica un filtro de mediana a una imagen para reducir el ruido.
    """
    filtered_image = median_filter(image, size)
    return filtered_image

def apply_gaussian_filter(image, sigma):
    """
    Aplica un filtro gaussiano a una imagen para suavizarla.
    """
    filtered_image = gaussian_filter(image, sigma)
    return filtered_image

def subtract_background(image, box_size):
    """
    Resta el fondo de una imagen utilizando una región de fondo local.
    """
    mean, median, std = sigma_clipped_stats(image)
    filtered_image = apply_median_filter(image, box_size)
    background_subtracted_image = image - filtered_image + median
    return background_subtracted_image

# Ejemplo de uso
image_path = 'ruta/a/la/imagen.fits'
image = load_fits_image(image_path)
display_image(image)

# Opciones de procesamiento
options = {
    'rescale': True,
    'rescale_range': (0, 255),
    'stretch': 'linear',
    'stretch_params': {},
    'median_filter': True,
    'median_filter_size': 3,
    'gaussian_filter': False,
    'gaussian_filter_sigma': 2,
    'subtract_background': True,
    'background_box_size': 50
}

# Procesar la imagen
processed_image = image.copy()

# Reescalar la imagen
if options.get('rescale'):
    processed_image = rescale_image(processed_image, scale_range=options['rescale_range'])

# Estirar la escala de la imagen
if options.get('stretch'):
    processed_image = stretch_image(processed_image, stretch=options['stretch'], **options['stretch_params'])

# Aplicar un filtro de mediana
if options.get('median_filter'):
    processed_image = apply_median_filter(processed_image, size=options['median_filter_size'])

# Aplicar un filtro gaussiano
if options.get('gaussian_filter'):
    processed_image = apply_gaussian_filter(processed_image, sigma=options['gaussian_filter_sigma'])

# Restar el fondo de la imagen
if options.get('subtract_background'):
    processed_image = subtract_background(processed_image, box_size=options['background_box_size'])

# Mostrar la imagen procesada
display_image(processed_image)
