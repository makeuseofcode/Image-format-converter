# Importing Library
from PIL import Image
 
# Loading the image
image = Image.open('sample-jpg-image.jpg')

# Converting image from JPG to PNG format
image.save("converted-png-image.png")

print("Image successfully converted!")