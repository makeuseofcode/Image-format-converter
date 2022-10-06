# Importing Library
from PIL import Image
 
try:
    # Loading the image
    image = Image.open('wrong-filename.jpg')

    # Converting image from JPG to PNG format
    image.save("converted-png-image.png")

    print("Image successfully converted!")

except FileNotFoundError:
    print("Couldn't find the provided image")
