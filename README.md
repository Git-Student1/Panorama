# Info
This code produces a panorama. To create non distorted panoramas the requirements explained below need to be met. 



# Context
Example: 
For a panorama taken with a camera that has a sensor length of 22.3x14.9mm and produces images in the format   1920x1080 and a focal length of 34 mm that was rotated by 90° for a larger Panorama height, you need around 19035 pixels to produce a non distorted 360° panorama.

* Formular: I_req = 1920pixels*360/(2*atan(22.3mm/(2*34mm)))

# Requirements to use this program 
## Image requirement
The requirements are very hard to meet, so this is a very niche panorama creation program. 

### Image Count
To properly use this code, you need a corresponding amount of  images (I_req)  taken in regular intervals to produce a non distorted panorama. If you only want a partial panorama, you can adjsust the 360° and recalulate. 


### Image recording
The Images must be taken by a camera that is rotating automatically on an arm. It might take many hours to produce a full 360° panorama and the area must be completely undistured and unchanged during this process to get a good panorama. 

## .Env
Also, add a .env file with the property PATH_TO_IMAGE_FOLDER and give it a value. 

