# OnePackLuck
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def load_fits_image(file_path, extension_name):
    """
    Carga una imagen en formato FITS desde un archivo.


    Args:
        file_path (str): Ruta del archivo FITS.
        extension_name (str): Nombre de la extensión que contiene la imagen.


    Returns:
        numpy.ndarray: Matriz de datos de la imagen FITS.
    """
    hdulist = fits.open(file_path)
    data = hdulist[extension_name].data
    hdulist.close()
    return data


def save_fits_image(data, file_path):
    """
    Guarda una imagen en formato FITS en un archivo.


    Args:
        data (numpy.ndarray): Matriz de datos de la imagen FITS.
        file_path (str): Ruta del archivo FITS de salida.
    """
    hdu = fits.PrimaryHDU(data)
    hdu.writeto(file_path, overwrite=True)


def load_jpg_image(file_path):
    """
    Carga una imagen en formato JPG desde un archivo.


    Args:
        file_path (str): Ruta del archivo JPG.


    Returns:
        numpy.ndarray: Matriz de datos de la imagen JPG.
    """
    image = Image.open(file_path)
    data = np.array(image)
    return data


def save_jpg_image(data, file_path):
    """
    Guarda una imagen en formato JPG en un archivo.


    Args:
        data (numpy.ndarray): Matriz de datos de la imagen JPG.
        file_path (str): Ruta del archivo JPG de salida.
    """
    image = Image.fromarray(data)
    image.save(file_path)


def apply_noise_reduction(data, threshold):
    """
    Aplica reducción de ruido a una imagen astronómica.


    Args:
        data (numpy.ndarray): Matriz de datos de la imagen.
        threshold (float): Umbral para la reducción de ruido.


    Returns:
        numpy.ndarray: Imagen con reducción de ruido.
    """
    # Aplicar la reducción de ruido a través de algún algoritmo o filtro específico
    # Aquí se muestra un ejemplo de reducción de ruido mediante umbralización
    noise_filtered = np.where(data < threshold, 0, data)
    return noise_filtered


def stack_images(images):
    """
    Apila varias imágenes astronómicas en una sola imagen.


    Args:
        images (list): Lista de imágenes astronómicas (matrices de datos).


    Returns:
        numpy.ndarray: Imagen apilada.
    """
    stacked_image = np.mean(images, axis=0)
    return stacked_image


def remove_gradients(data):
    """
    Elimina los gradientes presentes en una imagen astronómica.


    Args:
        data (numpy.ndarray): Matriz de datos de la imagen.


    Returns:
        numpy.ndarray: Imagen con gradientes eliminados.
    """
    # Aplicar algún algoritmo o método para eliminar gradientes
    # Aquí se muestra un ejemplo simple utilizando una imagen de referencia
    reference_image = load_fits_image('reference.fits')
    gradients_removed = data - reference_image
    return gradients_removed


def enhance_resolution(data, factor):
    """
    Mejora la resolución de una imagen astronómica.


    Args:
        data (numpy.ndarray): Matriz de datos de la imagen.
        factor (int): Factor de mejora de resolución.


    Returns:
        numpy.ndarray: Imagen con resolución mejorada.
    """
    # Aplicar algún algoritmo o técnica para mejorar la resolución
    # Aquí se muestra un ejemplo simple de aumento de tamaño mediante interpolación
    enhanced_data = np.kron(data, np.ones((factor, factor)))
    return enhanced_data


def enhance_details(data, strength):
    """
    Realza los detalles presentes en una imagen astronómica.


    Args:
        data (numpy.ndarray): Matriz de datos de la imagen.
        strength (float): Factor de realce de detalles.


    Returns:
        numpy.ndarray: Imagen con detalles realzados.
    """
    # Aplicar algún algoritmo o filtro específico para realzar detalles
    # Aquí se muestra un ejemplo simple de realce mediante multiplicación por un factor
    enhanced_data = data * strength
    return enhanced_data


def open_file_dialog():
    """
    Abre un diálogo de selección de archivo y retorna la ruta del archivo seleccionado.


    Returns:
        str: Ruta del archivo seleccionado.
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


# Ejemplo de uso:


# Cargar una imagen FITS
file_path = open_file_dialog()
fits_image = load_fits_image(file_path)


# Aplicar reducción de ruido
noise_threshold = 100
denoised_image = apply_noise_reduction(fits_image, noise_threshold)


# Apilar varias imágenes
stacked_images = [denoised_image, fits_image]
stacked_image = stack_images(stacked_images)


# Eliminar gradientes
gradients_removed_image = remove_gradients(stacked_image)


# Mejorar resolución
resolution_factor = 2
enhanced_resolution_image = enhance_resolution(gradients_removed_image, resolution_factor)


# Realzar detalles
details_strength = 1.5
enhanced_details_image = enhance_details(enhanced_resolution_image, details_strength)


# Guardar la imagen procesada
save_fits_image(enhanced_details_image, 'processed_image.fits')
