def on_draw(self, area, cr):
    if self.image:
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

        cr.save()
        cr.translate(translate_x, translate_y)
        cr.scale(scale_factor, scale_factor)

        # Draw the image
        Gdk.cairo_set_source_pixbuf(cr, self.image, 0, 0)
        cr.paint()

        cr.set_source_rgb(0.0, 0.0, 0.0)

        # Draw points with crosses inside
        for x, y in self.point_positions:
            cr.rectangle(x - 5, y - 5, 10, 10)
            cr.move_to(x - 5, y)
            cr.line_to(x + 5, y)
            cr.move_to(x, y - 5)
            cr.line_to(x, y + 5)
            cr.stroke()

        # Draw the outline of the full quadrilateral if four points are selected
        if len(self.point_positions) == 4:
            cr.move_to(*self.point_positions[0])
            for x, y in self.point_positions[1:]:
                cr.line_to(x, y)
            cr.close_path()
            cr.set_line_width(2)
            cr.stroke()

        cr.restore()
