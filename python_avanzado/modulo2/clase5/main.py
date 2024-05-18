from PIL import Image, ImageDraw
from PIL import ImageFont


def get_imgae(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)

        # image.show()
        # image_black = image.convert('L')
        # image_black.show() 
        # image_black.save("aaaBlack.jpg")

        font = ImageFont.truetype('fonts/Roboto-Bold.ttf', 120)
        draw = ImageDraw.Draw(image)
        draw.text(
            (500, 0), #tamaño 
            "Lean Gay", #Texto
            (255, 255, 255),
            font=font
        )
        image.show()
        image.save("aaaConTexto.jpg")

        #Creación thumbnail
        image.thumbnail((500, 500))
        image.show()
        image.save("aaaConThumbnail.jpg")

    except:
        print('NO SE ENCONTRO LA IMG')

if __name__ == '__main__':
    get_imgae("aaa.jpg")