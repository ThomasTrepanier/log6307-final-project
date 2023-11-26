def on_draw(self, area, cr):
    if self.image:
        # ...
        for image_x, image_y in self.point_positions:
            x, y = self.image_to_component_space(image_x, image_y)
            cr.rectangle(x - 5, y - 5, 10, 10)
            cr.move_to(x - 5, y)
            cr.line_to(x + 5, y)
            cr.move_to(x, y - 5)
            cr.line_to(x, y + 5)
            cr.stroke()
        # ...
