import numpy as np
from PIL import Image
import os

path_to_file ='tiff-files'

# path_to_file ='tiff-files2'

# path_to_file ='tiff-files3'

# path_to_file ='tiff-files5'

    
def stich_img(path_to_file, x , y):

    image = []
    for i in os.listdir(path_to_file):
            image.append(path_to_file+'/'+i)
    
    print(image)
         
    if len(image) >= x*y:
        pass
    
    else:
        # raise ValueError('not enough images in path_to_file !!!!!!!!!!!')
        raise ValueError('EXCEPTION not enough images in path_to_file !!!!!!!!!!!', x*y ,'images  needed : ', len(image),'images present !!!')
    
    
    image = image[:x*y] #-----> riduce lista immagini al numero richiesto
    
    
    with Image.open(image[0]) as img0:
        w, h = img0.size
   
    
    
    
    # new_image = np.zeros((4 * h, 3 * w)).astype('uint8')
    new_image = np.zeros((y * h, x * w)).astype('uint8')
    
    
     
    col = 0
    row = -1
    for i, imgs in enumerate(image):
        with Image.open(imgs) as img:
            if not i % x :
                row += 1
                col = 0
            img = np.array(img)
            new_image[row * h: (row + 1) * h, col * w: (col + 1) * w] = img
            col += 1
            
    

    
    image_pillow = Image.fromarray(new_image, mode = 'L')
    
    return image_pillow

img_stiched = stich_img(path_to_file, 3,5)   

# img_stiched.save('prova.tif', mode = 'L')


img_stiched.show()
