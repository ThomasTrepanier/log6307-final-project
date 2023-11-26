def get_pts(img):
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours, key=cv2.contourArea)
    peri = cv2.arcLength(cnt, True)
    return cv2.approxPolyDP(cv2.convexHull(cnt), 0.04 * peri, True)
