from PIL import Image
import os

path_to_file ='tiff-files'



def stich_tile(path_to_file, xx , yy):
    images = []
    for i in os.listdir(path_to_file):
            images.append(i)

    
    if len(images) >= xx*yy:
        pass
    
    else:
        raise ValueError('not enough images in path_to_file !!!!!!!!!!!')
        
    
    sq_x = xx
    sq_y = yy
    img_x = (Image.open(path_to_file+'/'+images[0]).size[0])
    img_y = (Image.open(path_to_file+'/'+images[0]).size[1])
    img_mode = (Image.open(path_to_file+'/'+images[0]).mode)
    
    new_image = Image.new(img_mode, (img_x*sq_x, img_y*sq_y))
    
    x = 0
    y = 0
    cnt = 0
    for i in images:
        with Image.open(path_to_file+'/'+i) as img:
            new_image.paste(img, (x,y))
            cnt += 1
            x += img_x 
            if cnt == sq_x:
                x = 0
                y += img_y
                cnt = 0
            else:
                pass
                
  
    return new_image
 

stich_tile(path_to_file, 3, 5).show()
