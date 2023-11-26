def on_motion_notify(self, widget, event):
    if self.dragging_point is not None:
        x, y = self.component_to_image_space(event.x, event.y)

        # Check for snapping to points with the same x or y coordinate
        for i, (px, py) in enumerate(self.point_positions):
            if i != self.dragging_point:
                if abs(px - x) < 10:
                    x = px
                if abs(py - y) < 10:
                    y = py

        self.point_positions[self.dragging_point] = (x, y)
        self.canvas_area.queue_draw()
