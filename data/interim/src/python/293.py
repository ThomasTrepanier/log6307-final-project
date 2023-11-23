def image_to_component_space(self, image_x, image_y):
    # Calculate the aspect ratio of the image and drawing area
    image_aspect_ratio = self.image.get_width() / self.image.get_height()
    drawing_area_width = self.canvas_area.get_allocated_width()
    drawing_area_height = self.canvas_area.get_allocated_height()
    drawing_area_aspect_ratio = drawing_area_width / drawing_area_height

    # Calculate the scaling factor to fit the image inside the drawing area
    if image_aspect_ratio > drawing_area_aspect_ratio:
        scale_factor = drawing_area_width / self.image.get_width()
    else:
        scale_factor = drawing_area_height / self.image.get_height()

    # Calculate the translation to center the image inside the drawing area
    translate_x = (drawing_area_width - self.image.get_width() * scale_factor) / 2
    translate_y = (drawing_area_height - self.image.get_height() * scale_factor) / 2

    # Apply scaling and translation to convert from image to component space
    x = image_x * scale_factor + translate_x
    y = image_y * scale_factor + translate_y

    return x, y
