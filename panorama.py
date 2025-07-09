import time
from PIL import Image
from  PIL.Image import Transpose
from pathlib import Path
import numpy as np
import cv2
from PIL import ImageDraw 
from PIL import ImageFont
from tqdm import tqdm



imgaes_path = Path("C:/Users/Maxim/Downloads/_PanoJPEG/_PanoJPEG").glob("*.jpg")
index =0
max_index = 5000

#values after rotation
image_width = 1080
image_width_center = image_width // 2
image_height = 1920





def create_panorama_image():
    new_image_pix = []
    index = 0
    for image_path in tqdm(imgaes_path):
        index+=1
        img = cv2.imread(image_path)
        new_image_pix.append( img[image_width_center, :])
        if index == max_index:
            return new_image_pix        

def save_image(pixels_array, time_for_panorama_creation):
    array = np.array(pixels_array, dtype=np.uint8)

    panorama_image = Image.fromarray(array).transpose(Transpose.ROTATE_270)
    draw = ImageDraw.Draw(panorama_image)
    font = ImageFont.load_default(30)
    draw.text((0, 0),f"time: {round(time_for_panorama_creation)} s",(0,0,0), font=font)
    panorama_image.save('panorama.png')
    panorama_image.show()

t0 = time.time()
pixels_array = create_panorama_image()
t1 = time.time()
time_for_panorama_creation = t1-t0
save_image(pixels_array, time_for_panorama_creation)





    


#im = Image.open('dead_parrot.jpg') # Can be many different formats.

