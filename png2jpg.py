# Importing Library
from PIL import Image
 
# Loading the image
image = Image.open('sample-png-image.png')

# Specifying the RGB mode to the image
image = image.convert('RGB')

# Converting image from PNG to JPG format
image.save("converted-jpg-image.jpg")

print("Image successfully converted!")