# OnePackLuck
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

def load_fits_image(file_path, extension_name):
"""
Carga una imagen en formato FITS desde un archivo.                                                                                                      Args:
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
data = np.array(image)                                                                                                                                                    return data

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
images (list): Lista de imágenes astronómicas (matrices de datos).                                                             Returns:
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
enhanced_data = np.kron(data, np.ones((factor, factor)))                                                                                           return enhanced_data

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
denoised_image = apply_noise_reduction(fits_image, noise_threshold)                                                                 # Apilar varias imágenes
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
# Crear la ventana principal
window = tk.Tk()
window.title("Procesamiento de Imagen FITS")
# Variables globales
fits_image = None
processed_image = None
# Funciones de los botones
def open_file():
global fits_image, processed_image
file_path = filedialog.askopenfilename()
fits_image = load_fits_image(file_path)
show_image(fits_image)
def process_image():
global processed_image
if fits_image is not None:
# Obtener los datos ingresados por el usuario
noise_threshold = float(entry_noise.get())
resolution_factor = int(entry_resolution.get())
details_strength = float(entry_details.get())
# Aplicar las opciones de procesamiento
denoised_image = apply_noise_reduction(fits_image, noise_threshold)
enhanced_resolution_image = enhance_resolution(denoised_image, resolution_factor)
enhanced_details_image = enhance_details(enhanced_resolution_image, details_strength)
processed_image = enhanced_details_image
# Mostrar la imagen procesada
show_image(processed_image)
print("Procesamiento de imagen completado.")
def save_processed_image():
global processed_image
if processed_image is not None:
file_path = filedialog.asksaveasfilename(defaultextension=".fits")
save_fits_image(processed_image, file_path)
print("Imagen procesada guardada.")
# Función para mostrar la imagen en la ventana                                                                                                           def show_image(image_data):
image = ImageTk.PhotoImage(image=Image.fromarray(image_data))
image_label.configure(image=image)
image_label.image = image
# Cargar una imagen FITS
btn_open_file = tk.Button(window, text="Abrir archivo FITS", command=open_file)
btn_open_file.pack()
# Parámetros de procesamiento
label_noise = tk.Label(window, text="Umbral de ruido:")
label_noise.pack()
entry_noise = tk.Entry(window)
entry_noise.pack()
label_resolution = tk.Label(window, text="Factor de resolución:")
label_resolution.pack()
entry_resolution = tk.Entry(window)
entry_resolution.pack()
label_details = tk.Label(window, text="Fuerza de detalles:")
label_details.pack()
entry_details = tk.Entry(window)
entry_details.pack()
# Botones de procesamiento
btn_process = tk.Button(window, text="Procesar imagen", command=process_image)
btn_process.pack()
btn_save = tk.Button(window, text="Guardar imagen procesada", command=save_processed_image)
btn_save.pack()
# Visualización de imagen
image_label = tk.Label(window)
image_label.pack()
# Ejecutar la interfaz de usuario
window.mainloop()
pip install astropy astroquery
from astropy.coordinates import SkyCoord
from astropy import units as u
from astroquery.lroc import LROC
# Coordenadas de la Luna
lunar_coords = SkyCoord(0*u.deg, 0*u.deg, frame='icrs')
# Consulta de imágenes FITS
result = LROC.query_lroc_by_coords(lunar_coords, radius=1*u.deg)
# Descargar la primera imagen FITS
if result:
image_data = LROC.download(result[0], download_dir='fits_images')
print("Imagen FITS descargada:", image_data)
else:
print("No se encontraron imágenes FITS para las coordenadas de la Luna.")age.fits')
