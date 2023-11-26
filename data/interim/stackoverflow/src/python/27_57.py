def get_edges(img):
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  bitwised_img = cv2.bitwise_not(gray_img)
  guassian_img = cv2.GaussianBlur(bitwised_img, (5, 5), 0)
  bilateral_img = cv2.bilateralFilter(guassian_img, 11, 17, 17)
  t, thresh_bin = cv2.threshold(bilateral_img, 0, 255, cv2.THRESH_OTSU)
  canny = cv2.Canny(thresh_bin, 0.5 * t, t)
  dilated = cv2.dilate(canny,
                       cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3)))
  medianed = cv2.medianBlur(dilated, 3)
  # Edges will be discontinous so dialtion will be make them contionuous
  return medianed

