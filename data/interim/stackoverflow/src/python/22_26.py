import cv2

def lighten(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    v = hsv[..., 2]
    v[:] = cv2.add(v, value)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)[1] == 0
img[mask] = lighten(img)[mask]
cv2.imshow("result", img)
cv2.waitKey(0)
