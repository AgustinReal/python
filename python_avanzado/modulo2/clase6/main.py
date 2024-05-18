from PIL import Image
import os

def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(image_folder + file)
            print("Comprimiento el archivo" + file_name + file_extension)

            if file_extension == '.png':
                file_compress = Image.open(image_folder + file)
                file_compress.save(file_name + "comprimido.png", 
                                   optimize=True,
                                   quality=70)
    except:
        print("No se pudo comprimir")

if __name__ == '__main__':
    compress_images('C:\\Users\\Usuario\\Pictures\\QR\\')
