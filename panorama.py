import math
import os
import time
from PIL import Image
from  PIL.Image import Transpose
from pathlib import Path
import numpy as np
from PIL import ImageDraw 
from PIL import ImageFont
from tqdm import tqdm
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv() 

image_paths = list(Path(os.getenv("PATH_TO_IMAGE_FOLDER")).glob("*.jpg")) # list is important as it retures a generator, once consumed you cannot get/access the image paths again
index =0
max_index = 1000

#values after rotation
image_width = 1080
image_width_center = image_width // 2
image_height = 1920
count_images = len(image_paths)

def create_panorama_image_detailed():
    new_image_pix = []
    for image_path in tqdm(image_paths, total=count_images):
        img = Image.open(image_path)
        pix = img.load()
        line = []
        for y in range(image_height):
            line.append(pix[y, image_width_center])
        new_image_pix.append(line)
    return new_image_pix        

def create_panorama_image_aproximated(approximation_width:int=5):
    new_image_pix = []
    i = 0
    image_path_list = image_paths[::approximation_width]

    for image_path in tqdm(image_path_list, total=len(image_path_list)):
        max_index_addition = (approximation_width-1)//2
        img = Image.open(image_path)
        pix = img.load()
        
        for p in range(-max_index_addition, max_index_addition+1,1):
                line = []
                for y in range(image_height):
                    line.append(pix[y, image_width_center+p])
                i += 1
                new_image_pix.append(line)
    return new_image_pix   

def create_panorama_image_stereo():
    new_image_pix = [[(0,0,0) for _ in range(image_height)] for _ in range(count_images)] # [[(0,0,0)]*image_height]*1000 causes shallow copies! All rows are the same and get changed as one row changes!
    #new_image_pix = []
    index = 0
    focal_length = 34 # in mm
    stereo_basis = 64 # in mm, simulating the distance between the two eyes
    radius_of_camera_rotation = 328 # in mm, distance from the camera to the center of rotation
    sensor_width = 14.9 # in mm, length of the camera sensor in width direction
    s= focal_length* math.tan(math.asin(stereo_basis/radius_of_camera_rotation)) # in mm
    s_column = round(s*(image_width//sensor_width))
    pbar = tqdm(total=count_images, desc="Creating panorama image")
    while index < count_images:
        pbar.update(1)
        image_path = image_paths[index]
        img = Image.open(image_path)
        pix = img.load()
        # stereo separates green + blue & red values
        for y in range(image_height):
            # add green and blue values to a bit from the left 
            green_blue_index = index-s_column//2
            if green_blue_index >= count_images:
                green_blue_index = count_images-green_blue_index
            new_image_pix[green_blue_index][y] =  (new_image_pix[index][y][0], pix[y, image_width_center][1], pix[y, image_width_center][2])
            red_index = index+s_column//2
            # add red values to a bit from the right 
            if red_index >= count_images:
                red_index = count_images-red_index
            new_image_pix[red_index][y] =  (pix[y, image_width_center][0], new_image_pix[red_index][y][1], new_image_pix[red_index][y][2] )
        index+=1
    pbar.close()
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
pixels_array = create_panorama_image_aproximated(99)
t1 = time.time()
time_for_panorama_creation = t1-t0
save_image(pixels_array, time_for_panorama_creation)