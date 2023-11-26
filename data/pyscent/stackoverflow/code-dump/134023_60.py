# imports 
import numpy as np
import cv2

width = height = 600 # normal passport photo size in pixels

# global variable that will update the points when we clicked on the image
pt1 = []
pt2 = np.float32([[0, 0], [height, 0], [0, width], [height, width]])
def mouseEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pt1
        if len(pt1) == 4:
            pt1 = []
        else:
            pt1.append([x, y])

while 1:
    image = cv2.imread("img.jpg", cv2.IMREAD_UNCHANGED)
    cv2.imshow("Original Image", image)
    cv2.setMouseCallback("Original Image", mouseEvent)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if len(pt1) == 4:
        break
