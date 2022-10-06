# Importing Library
from PIL import Image
 
# Loading the transparent GIF image
image = Image.open('sample-transparent-gif-image.gif')

# Converting an image from GIF to PNG format
image.save("converted-png-image.png")

print("Image successfully converted!")