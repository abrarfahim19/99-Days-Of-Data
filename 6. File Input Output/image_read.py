import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save("myimage.gif", save_all = True, append_images = [*images[0:]],duration=200,loop=0)