import cv2
import numpy as np

def intersected(img, masks):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for lower, upper in masks:
        mask = cv2.inRange(img_hsv, np.array(lower), np.array(upper))
        blur = cv2.GaussianBlur(mask, (5, 5), 0)
        canny = cv2.Canny(blur, 0, 0)
        contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        count = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > 50:
                cv2.drawContours(img, [cnt], -1, (0, 255, 0), 1)
                cv2.imshow("Test", img)
                count += 1
                if count == 2:
                    return True

img = cv2.imread("shapes.png")

blue_mask = [1, 0, 0], [178, 255, 255]
red_mask = [0, 1, 0], [179, 254, 255]

if intersected(img, (blue_mask, red_mask)):
    print("Intersection detected!")
else:
    print("No intersection detected.")
