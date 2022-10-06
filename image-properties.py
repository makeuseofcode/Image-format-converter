# Importing library
from PIL import Image

# Loading the image 
image = Image.open('sample-image.jpg')

# Prints the name of the file 
print("Filename: ", image.filename)

# Prints the fomat of the file. 
# Eg- PNG, JPG, GIF, etc.
print("Format: ", image.format)

# Prints the mode of the file
# Eg- RGB, RFBA, CMYK, etc.
print("Mode: ", image.mode)

# Prints the size as a width, height tuple (in pixels)
print("Size: ", image.size)

# Prints the width of the image (in pixels)
print("Width: ", image.width)

# Prints the height  of the image (in pixels)
print("Height: ", image.height)

# Closing the image 
image.close()