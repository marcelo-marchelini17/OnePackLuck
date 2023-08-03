# OnePackLuck
## Procesamiento de Imágenes FITS
#### Este es un programa de procesamiento de imágenes FITS que incluye una interfaz gráfica para cargar, procesar y guardar imágenes FITS. El programa está escrito en Python y utiliza la biblioteca Tkinter para la interfaz gráfica y NumPy, Matplotlib y Astropy para el procesamiento de imágenes.

## Estructura de Carpetas
#### La estructura de carpetas y archivos:

OnePackLuck/

├── OnePackLuck/

│   ├── __init__.py

│   ├── CodeOnePackLuck.py

├── pyproject.toml

├── LICENSE

├── README.md

└── setup.py

## Instalación
Para instalar el paquete, asegúrate de tener Python 3.6 o superior y ejecuta el siguiente comando en la terminal:

pip install OnePackLuck==0.1

## Uso

Una vez instalado el paquete "OnePackLuck" que contiene el archivo llamado "CodeOnePackLuck.py". En el que están definidas varias funciones útiles relacionadas con el procesamiento de imágenes. Se puede proseguir a usar el paquete de la siguiente manera: 

1. Primero, asegúrate de que hayas instalado el paquete "OnePackLuck" correctamente utilizando el comando `pip install OnePackLuck==0.1`.

2. Luego, en tu script, puedes importar las funciones que necesitas de esta manera:

from OnePackLuck.CodeOnePackLuck import (
    load_fits_image,
    save_fits_image,
    load_jpg_image,
    save_jpg_image,
    apply_noise_reduction,
    stack_images,
    remove_gradients,
    enhance_resolution,
    enhance_details,
    open_file_dialog
)

3. Ahora, puedes utilizar estas funciones en tu código como se muestra a continuación:                                                                                                                                                                                                                                                              
# Cargar una imagen FITS
fits_image = load_fits_image('ruta_de_la_imagen.fits')

# Aplicar reducción de ruido a la imagen FITS
threshold = 50  # Umbral de ruido
denoised_image = apply_noise_reduction(fits_image, threshold)

# Mejorar la resolución de la imagen
factor = 2  # Factor de mejora de resolución
enhanced_image = enhance_resolution(denoised_image, factor)

# Mejorar los detalles de la imagen
strength = 1.5  # Fuerza de mejora de detalles
enhanced_details_image = enhance_details(enhanced_image, strength)

# Guardar la imagen procesada como FITS
save_fits_image(enhanced_details_image, 'imagen_procesada.fits')

# Cargar una imagen JPG
jpg_image = load_jpg_image('ruta_de_la_imagen.jpg')

# Aplicar una función de procesamiento específica
processed_jpg_image = stack_images([jpg_image, enhanced_details_image])

# Guardar la imagen procesada como JPG
save_jpg_image(processed_jpg_image, 'imagen_procesada.jpg')

# ... y así sucesivamente para otras funciones

Recuerda reemplazar `'ruta_de_la_imagen.fits'` y `'ruta_de_la_imagen.jpg'` con las rutas adecuadas de tus propias imágenes.

Este es un ejemplo básico de cómo usar las funciones del paquete "OnePackLuck" en tu código. Puedes adaptar este esquema a tus necesidades específicas de procesamiento de imágenes.

También puedes llamar directamente a la interfaz de usuario desde tu terminal en un lector de lenguaje de programacion, como visual, spyder, notepad++, o desde el cmd de Windows ejecutando la siguiente línea de código: from OnePackLuck.CodeOnePackLuck import apply_noise_reduction, enhance_resolution, enhance_details

Sin embargo, ten en cuenta que ello solo importa las funciones apply_noise_reduction, enhance_resolution y enhance_details desde el módulo CodeOnePackLuck. Si deseas acceder a otras funciones definidas en el mismo módulo, deberás importarlas de manera similar.

## Licencia
#### Este proyecto está bajo la Licencia MIT.
