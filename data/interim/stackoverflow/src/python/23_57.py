import cv2
import numpy as np

def process(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (1, 1), 1)
    img_canny = cv2.Canny(img_blur, 350, 150)
    kernel = np.ones((3, 3))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    return cv2.erode(img_dilate, kernel, iterations=1)

def get_pts(img):
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours, key=cv2.contourArea)
    peri = cv2.arcLength(cnt, True)
    return cv2.approxPolyDP(cv2.convexHull(cnt), 0.04 * peri, True)

files = ["1.jpg", "2.jpg", "3.jpg"]
width, height = 350, 450
pts2 = np.float32([[width, 0], [0, 0], [width, height], [0, height]])

for file in files:
    img = cv2.imread(file)
    pts1 = get_pts(process(img)).squeeze()
    pts1 = np.float32(pts1[np.lexsort(pts1.T)])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    out = cv2.warpPerspective(img, matrix, (width, height))[5:-5, 5:-5]
    cv2.imshow(file, out)

cv2.waitKey(0)
cv2.destroyAllWindows()
