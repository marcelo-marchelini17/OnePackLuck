import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from astropy.coordinates import SkyCoord
from astropy import units as u

def load_fits_image(file_path, extension_name='PRIMARY'):
    """
    Carga una imagen FITS desde el archivo especificado y devuelve los datos.

    Parameters:
    file_path (str): Ruta al archivo FITS.
    extension_name (str, optional): Nombre de la extensión FITS a cargar. Por defecto es 'PRIMARY'.

    Returns:
    numpy.ndarray: Datos de la imagen FITS cargada.
    """
    hdulist = fits.open(file_path)
    data = hdulist[extension_name].data  # Usa la extensión adecuada
    hdulist.close()
    print(data)
    plt.imshow(data)
    plt.show()
    return data

def save_fits_image(data, file_path):
    """
    Guarda los datos de la imagen en formato FITS en el archivo especificado.

    Parameters:
    data (numpy.ndarray): Datos de la imagen a guardar.
    file_path (str): Ruta al archivo FITS de destino.
    """
    hdu = fits.PrimaryHDU(data)
    hdu.writeto(file_path, overwrite=True)

def load_jpg_image(file_path):
    """
    Carga una imagen en formato JPG desde el archivo especificado y devuelve los datos.

    Parameters:
    file_path (str): Ruta al archivo JPG.

    Returns:
    numpy.ndarray: Datos de la imagen JPG cargada.
    """
    image = Image.open(file_path)
    data = np.array(image)
    return data

def save_jpg_image(data, file_path):
    """
    Guarda los datos de la imagen en formato JPG en el archivo especificado.

    Parameters:
    data (numpy.ndarray): Datos de la imagen a guardar.
    file_path (str): Ruta al archivo JPG de destino.
    """
    image = Image.fromarray(data)
    image.save(file_path)

def apply_noise_reduction(data, threshold):
    """
    Aplica reducción de ruido a los datos de la imagen.

    Parameters:
    data (numpy.ndarray): Datos de la imagen a procesar.
    threshold (float): Umbral de reducción de ruido.

    Returns:
    numpy.ndarray: Datos de la imagen con reducción de ruido aplicada.
    """
    noise_filtered = np.where(data < threshold, 0, data)
    return noise_filtered

def stack_images(images):
    """
    Apila un conjunto de imágenes.

    Parameters:
    images (list): Lista de matrices de imágenes a apilar.

    Returns:
    numpy.ndarray: Imagen apilada resultante.
    """
    stacked_image = np.mean(images, axis=0)
    return stacked_image

def remove_gradients(data):
    """
    Elimina gradientes en la imagen usando una imagen de referencia.

    Parameters:
    data (numpy.ndarray): Datos de la imagen a procesar.

    Returns:
    numpy.ndarray: Datos de la imagen con gradientes eliminados.
    """
    reference_image = load_fits_image('reference.fits')
    gradients_removed = data - reference_image
    return gradients_removed

def enhance_resolution(data, factor):
    """
    Mejora la resolución de la imagen.

    Parameters:
    data (numpy.ndarray): Datos de la imagen a procesar.
    factor (int): Factor de mejora de resolución.

    Returns:
    numpy.ndarray: Datos de la imagen con resolución mejorada.
    """
    enhanced_data = np.kron(data, np.ones((factor, factor)))
    return enhanced_data

def enhance_details(data, strength):
    """
    Realza los detalles de la imagen.

    Parameters:
    data (numpy.ndarray): Datos de la imagen a procesar.
    strength (float): Fuerza de realce de detalles.

    Returns:
    numpy.ndarray: Datos de la imagen con detalles realzados.
    """
    enhanced_data = data * strength
    return enhanced_data

def open_file_dialog():
    """
    Abre un diálogo de selección de archivo.

    Returns:
    str: Ruta al archivo seleccionado.
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Crear la ventana principal
window = tk.Tk()
window.title("Procesamiento de Imagen FITS")
window.configure(bg="blue")  # Color de fondo azul

# Variables globales
fits_image = None
processed_image = None

# Funciones de los botones
def open_file():
    """
    Abre un cuadro de diálogo para seleccionar un archivo FITS, carga la imagen y la muestra en pantalla.

    Global Variables:
    fits_image (numpy.ndarray): Variable global para almacenar la imagen FITS cargada.

    Side Effects:
    Muestra la imagen FITS en pantalla usando la función show_image().
    """
    global fits_image, processed_image
    file_path = filedialog.askopenfilename()
    fits_image = load_fits_image(file_path)
    show_image(fits_image)

def process_image(): 
    """
    Procesa la imagen FITS cargada con los parámetros especificados y muestra la imagen procesada en pantalla.

    Global Variables:
    fits_image (numpy.ndarray): Variable global que almacena la imagen FITS cargada.
    processed_image (numpy.ndarray): Variable global para almacenar la imagen procesada.

    Side Effects:
    Muestra la imagen procesada en pantalla usando la función show_image().
    """
    global processed_image
    if fits_image is not None:
       noise_threshold = float(entry_noise.get())
       resolution_factor = int(entry_resolution.get())
       details_strength = float(entry_details.get())
       denoised_image = apply_noise_reduction(fits_image, noise_threshold)
       enhanced_resolution_image = enhance_resolution(denoised_image, resolution_factor)
       enhanced_details_image = enhance_details(enhanced_resolution_image, details_strength)
       processed_image = enhanced_details_image
       show_image(processed_image)
       print("Procesamiento de imagen completado.")

def save_processed_image():
    """
    Guarda la imagen procesada en formato FITS en la ubicación especificada por el usuario.

    Global Variables:
    processed_image (numpy.ndarray): Variable global que almacena la imagen procesada.

    Side Effects:
    Guarda la imagen procesada en un archivo FITS usando la función save_fits_image().
    Imprime un mensaje indicando que la imagen procesada ha sido guardada.
    """
    global processed_image
    if processed_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".fits")
        save_fits_image(processed_image, file_path)
        print("Imagen procesada guardada.") 

def show_image(image_data):
    """
    Muestra la imagen dada en pantalla utilizando la biblioteca Matplotlib y la librería PIL para la interfaz gráfica.

    Parameters:
    image_data (numpy.ndarray): Datos de la imagen a mostrar.

    Side Effects:
    Muestra la imagen en la interfaz gráfica y en una ventana emergente usando Matplotlib.
    """
    image = Image.fromarray(image_data)

    # Convert to PhotoImage
    photo_image = ImageTk.PhotoImage(image=image)

    # Update the label with the new image
    image_label.configure(image=photo_image)
    image_label.image = photo_image

    # Show the processed image using matplotlib
    plt.imshow(image_data, cmap='gray')  # You can choose a suitable colormap here
    plt.show()

# Botones de la interfaz
btn_open_file = tk.Button(window, text="Abrir archivo FITS", command=open_file, bg="lightblue")
btn_open_file.pack(pady=5)

# Parámetros de procesamiento
params_frame = tk.Frame(window, bg="blue")
params_frame.pack(pady=10)
label_noise = tk.Label(params_frame, text="Umbral de ruido:", bg="blue", fg="white")
label_noise.pack(side="left")
entry_noise = tk.Entry(params_frame)
entry_noise.pack(side="left", padx=5)
label_resolution = tk.Label(params_frame, text="Factor de resolución:", bg="blue", fg="white")
label_resolution.pack(side="left")
entry_resolution = tk.Entry(params_frame)
entry_resolution.pack(side="left", padx=5)
label_details = tk.Label(params_frame, text="Fuerza de detalles:", bg="blue", fg="white")
label_details.pack(side="left")
entry_details = tk.Entry(params_frame)
entry_details.pack(side="left", padx=5)

# Botones de procesamiento
btn_process = tk.Button(window, text="Procesar imagen", command=process_image, bg="lightblue")
btn_process.pack(pady=5)
btn_save = tk.Button(window, text="Guardar imagen procesada", command=save_processed_image, bg="lightblue")
btn_save.pack(pady=5)

# Visualización de imagen
image_label = tk.Label(window, bg="blue")
image_label.pack(pady=10)

# Ejecutar la interfaz de usuario
window.mainloop()