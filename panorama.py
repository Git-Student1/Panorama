import time
from PIL import Image
from  PIL.Image import Transpose
from pathlib import Path
import numpy as np
import cv2

imgaes_path = Path("C:/Users/Maxim/Downloads/_PanoJPEG/_PanoJPEG").glob("*.jpg")
index =0
max_index = 1000

#values after rotation
image_width = 1080
image_width_center = image_width // 2
image_height = 1920

new_image_pix = []


t0 = time.time()


for image_path in imgaes_path:
    index+=1

    img = cv2.imread(image_path)
    new_image_pix.append( img[image_width_center, :])

    if index == max_index:
        break

t1 = time.time()
print(f"time: {t1-t0}")
# https://stackoverflow.com/questions/46923244/how-to-create-image-from-a-list-of-pixel-values-in-python3
# Convert the pixels into an array using numpy
array = np.array(new_image_pix, dtype=np.uint8)
# Use PIL to create an image from the new array of pixels
panorama_image = Image.fromarray(array).transpose(Transpose.ROTATE_270)
panorama_image.save('panorama.png')
panorama_image.show()


    


#im = Image.open('dead_parrot.jpg') # Can be many different formats.

