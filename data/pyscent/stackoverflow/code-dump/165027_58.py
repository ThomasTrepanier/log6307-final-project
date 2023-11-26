def validate_contour(img, cc):
  """Check if the contour is a good predictor of photo location. 
 Here you need to address some realtionship to find the table contour"""
  x, y, w, h = cv2.boundingRect(cc)
  if (170000<area <200000) and 500<h<600 and 300<w<400:
    return True
  return False
  
def get_contours(img):
  contours, hierarchy = cv2.findContours(edges, 1,
                                         2)
  # filter contours that are too large or small
  # print('not_filtered_contours_contours',contours)
  contours = [cc for cc in contours if validate_contour(img, cc)]
  return contours
