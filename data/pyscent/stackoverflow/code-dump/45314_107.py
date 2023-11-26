import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.spatial import cKDTree
import cv2
from scipy.ndimage.morphology import binary_fill_holes

def counter_clockwise_order(a, DEBUG_PLOT=False):
    b = a-a.min(0)
    d = pdist(b).min()
    c = np.round(2*b/d).astype(int)

    img = np.zeros(c.max(0)[::-1]+1, dtype=np.uint8)

    d1,d2 = cKDTree(c).query(c,k=3)
    b = c[d2]
    p1,p2,p3 = b[:,0],b[:,1],b[:,2]
    for i in range(len(b)):    
        cv2.line(img,tuple(p1[i]),tuple(p2[i]),255,1)
        cv2.line(img,tuple(p1[i]),tuple(p3[i]),255,1)

    img = (binary_fill_holes(img==255)*255).astype(np.uint8)   
    if int(cv2.__version__.split('.')[0])>=3:
        _,contours,hierarchy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    else:
        contours,hierarchy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cont = contours[0][:,0]        
    f1,f2 = cKDTree(cont).query(c,k=1)
    ordered_points = a[f2.argsort()[::-1]]

    if DEBUG_PLOT==1:
        NPOINTS = len(ordered_points)
        for i in range(NPOINTS):
            plt.plot(ordered_points[i:i+2,0],ordered_points[i:i+2,1],alpha=float(i)/(NPOINTS-1),color='k')
        plt.show()
    return ordered_points
