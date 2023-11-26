def process(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (1, 1), 1)
    img_canny = cv2.Canny(img_blur, 350, 150)
    kernel = np.ones((3, 3))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    return cv2.erode(img_dilate, kernel, iterations=1)
