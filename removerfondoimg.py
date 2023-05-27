#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from rembg import remove
from PIL import Image

def main():
    input_folder = "imagenes"
    output_folder = "imagenesSinFondo"
    
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Recorre todas las imágenes en la carpeta de entrada
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            # Carga la imagen de entrada
            input_image = Image.open(input_path)
            
            # Elimina el fondo de la imagen
            output_image = remove(input_image)
            
            # Guarda la imagen sin fondo en la carpeta de salida con el mismo nombre que la imagen original
            output_path = os.path.join(output_folder, filename.split('.')[0] + "SinFondo.png")
            output_image.save(output_path)

if __name__ == "__main__":
    main()