# Importing Library
from PIL import Image
 
# Loading the image
image = Image.open('sample-transparent-png-image.png')

# Converting an image from PNG to WEBP format
image.save("converted-webp-image.webp")

print("Image successfully converted!")