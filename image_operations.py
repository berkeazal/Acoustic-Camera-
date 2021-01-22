import os
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



# tuplenin carpimi
def multiply(tp):
    return int(tp*1.8)


#iki tuple nin toplami 
def sum(tp,tp2):
    return int(tp+tp2)

   


CWD= os.getcwd().replace("\\","/")

# sol ust image 
base_image_name = CWD+"/sol_ust.jpg"
mask_name = CWD+"/resized_result.png" 
base_image = Image.open(base_image_name)
mask_image = Image.open(mask_name)
rgb_mask_image = mask_image.convert('RGB')
resized_mask_image = rgb_mask_image.resize((1600, 1200))  # orjinal imaj resize ediliyor
base_image_pixels = base_image.load()
mask_image_pixels = resized_mask_image.load()

# sag alt image 
base_image_name_sag = CWD+"/sag_alt.jpg"
mask_name_sag = CWD+"/cikti_sag_alt.png" 
base_image_sag = Image.open(base_image_name_sag)
mask_image_sag = Image.open(mask_name_sag)
rgb_mask_image_sag = mask_image_sag.convert('RGB')
resized_mask_image_sag = rgb_mask_image_sag.resize((1600, 1200))  # orjinal imaj resize ediliyor
base_image_pixels_sag = base_image_sag.load()
mask_image_pixels_sag = resized_mask_image_sag.load()

# orta image 
base_image_name_orta = CWD+"/orta.jpg"
mask_name_orta = CWD+"/cikti_orta.png" 
base_image_orta = Image.open(base_image_name_orta)
mask_image_orta = Image.open(mask_name_orta)
rgb_mask_image_orta = mask_image_orta.convert('RGB')
resized_mask_image_orta = rgb_mask_image_orta.resize((1600, 1200))  # orjinal imaj resize ediliyor
base_image_pixels_orta = base_image_orta.load()
mask_image_pixels_orta = resized_mask_image_orta.load()


"""
for y in range(base_image.size[1]):
    for x in range(base_image.size[0]):
        sonuc1 = tuple(map(multiply,base_image_pixels[x,y]))
        sonuc2 = tuple(map(multiply,mask_image_pixels[x,y]))
        sonuc3 = tuple(map(sum,sonuc1,sonuc2))
        base_image_pixels[x,y] = sonuc3

base_image.save("islenmis_image.png")


imaj resize edip kayıt deneme
image= Image.open("test.png")
new_image = image.resize((1600, 1200))

new_image.save('buyuk.png')

"""

"""
sol ust için
second_image= base_image.copy()
second_image_pixels= second_image.load()

for y in range(base_image.size[1]):
    for x in range(base_image.size[0]):
        if (mask_image_pixels[x,y] == (68,1,84)):
            second_image_pixels[x,y] = base_image_pixels[x,y]
        else:
            sonuc1 = tuple(base_image_pixels[x,y])
            sonuc2 = tuple(mask_image_pixels[x,y])
            sonuc3 = tuple(map(sum,sonuc1,sonuc2))
            second_image_pixels[x,y] = sonuc3
        
            
second_image.save("islenmis_image3.png")
"""
"""
sag
second_image= base_image_sag.copy()
second_image_pixels= second_image.load()

for y in range(base_image_sag.size[1]):
    for x in range(base_image_sag.size[0]):
        if (mask_image_pixels_sag[x,y] == (68,1,84)):
            second_image_pixels[x,y] = base_image_pixels_sag[x,y]
        else:
            sonuc1 = tuple(base_image_pixels_sag[x,y])
            sonuc2 = tuple(mask_image_pixels_sag[x,y])
            sonuc3 = tuple(map(sum,sonuc1,sonuc2))
            second_image_pixels[x,y] = sonuc3
        
            
second_image.save("sag.png")

"""
second_image= base_image_orta.copy()
second_image_pixels= second_image.load()

for y in range(base_image_orta.size[1]):
    for x in range(base_image_orta.size[0]):
        if (mask_image_pixels_orta[x,y] == (68,1,84)):
            second_image_pixels[x,y] = base_image_pixels_orta[x,y]
        else:
            sonuc1 = tuple(base_image_pixels_orta[x,y])
            sonuc2 = tuple(map(multiply,mask_image_pixels_orta[x,y]))
            sonuc3 = tuple(map(sum,sonuc1,sonuc2))
            second_image_pixels[x,y] = sonuc3
        
            
second_image.save("orta.png")







