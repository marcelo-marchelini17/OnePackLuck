# OnePackLuck
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from astropy.coordinates import SkyCoord
from astropy import units as u

def load_fits_image(file_path, extension_name='PRIMARY'):
    hdulist = fits.open(file_path)
    data = hdulist[extension_name].data  # Usa la extensión adecuada
    hdulist.close()
    print(data)
    plt.imshow(data)
    plt.show()
    return data

def save_fits_image(data, file_path):
    hdu = fits.PrimaryHDU(data)
    hdu.writeto(file_path, overwrite=True)

def load_jpg_image(file_path):
    image = Image.open(file_path)
    data = np.array(image)
    return data

def save_jpg_image(data, file_path):
    image = Image.fromarray(data)
    image.save(file_path)

def apply_noise_reduction(data, threshold):
    noise_filtered = np.where(data < threshold, 0, data)
    return noise_filtered

def stack_images(images):
    stacked_image = np.mean(images, axis=0)
    return stacked_image

def remove_gradients(data):
    reference_image = load_fits_image('reference.fits')
    gradients_removed = data - reference_image
    return gradients_removed

def enhance_resolution(data, factor):
    enhanced_data = np.kron(data, np.ones((factor, factor)))
    return enhanced_data

def enhance_details(data, strength):
    enhanced_data = data * strength
    return enhanced_data

def open_file_dialog():
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
    global fits_image, processed_image
    file_path = filedialog.askopenfilename()
    fits_image = load_fits_image(file_path)
    show_image(fits_image)

def process_image():
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
    global processed_image
    if processed_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".fits")
        save_fits_image(processed_image, file_path)
        print("Imagen procesada guardada.")

def show_image(image_data):
    image = ImageTk.PhotoImage(image=Image.fromarray(image_data))
    image_label.configure(image=image)
    image_label.image = image

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
