    #!/usr/bin/env python3
import numpy as np
from imageio import imread, imwrite
from pathlib import Path


def tile_images(images, cols):
    """Tile images of same size to grid with given number of columns.
    
    Args:
        images (collection of ndarrays)
        cols (int): number of colums 
    
    Returns:
        ndarray: stitched image
    """
    images = iter(images)
    first = True
    rows = []
    i = 0
    while True:
        
        try:
            im = next(images)
            print(f"add image, shape: {im.shape}, type: {im.dtype}")
        except StopIteration:
            if first:
                break
            else:
                im = np.zeros_like(im)  # black background
                
        if first:
            row = im  # start next row
            first = False  
        else:    
            row = np.concatenate((row, im), axis=1)  # append to row
            
        i += 1
        if not i % cols:
            print(f"row done, shape: {row.shape}")
            rows.append(row) # finished row
            first = True
            
    tiled = np.concatenate(rows)   # stitch rows    
    return tiled        

def main():
    images = (imread(f) for f in Path().glob("*.*") if f.suffix in (".jpg", ".png") if f.name != "new.png") 
    new = tile_images(images, cols=3)
    imwrite("new.png", new)


def test():
    im1 = np.arange(65536).reshape(256,256)
    im2 = np.arange(65536/2).reshape(128,256)
    
    images = [im1,im1,im1,im2,im2,im2]
    
    # works
    new = tile_images(images, 3)
    imwrite("new.png", new)
    
    # failes
    new = tile_images(images, 2)
    imwrite("new2.png", new)
    
    
if __name__ == "__main__":
    main()
    # test()
