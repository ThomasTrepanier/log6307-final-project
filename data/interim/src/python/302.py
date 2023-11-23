def on_motion_notify(self, widget, event):
    if self.dragging_point is not None:
        x, y = self.component_to_image_space(event.x, event.y)
        width = self.image.get_width()
        height = self.image.get_height()

        # Check for snapping to points with the same x or y coordinate
        for i, (px, py) in enumerate(self.point_positions):
            if i != self.dragging_point:
                if abs(px - x) < ALIGN_SNAP_SIZE:
                    x = px
                if abs(py - y) < ALIGN_SNAP_SIZE:
                    y = py

        # Check for snapping to the image borders
        if abs(x) < ALIGN_SNAP_SIZE:
            x = 0
        elif abs(x - width) < ALIGN_SNAP_SIZE:
            x = width
        if abs(y) < ALIGN_SNAP_SIZE:
            y = 0
        elif abs(y - height) < ALIGN_SNAP_SIZE:
            y = height

        self.point_positions[self.dragging_point] = (x, y)
        self.canvas_area.queue_draw()
