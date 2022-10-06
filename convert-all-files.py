from PIL import Image
import glob
for file in glob.glob("images/*.jpg"):
    image = Image.open(file)
    image.save(file.replace("jpg", "png"))