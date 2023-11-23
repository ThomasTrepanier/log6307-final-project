import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class Select2DApp(Gtk.Window):
    # ... (previous code remains unchanged)

    def on_button_press(self, widget, event):
        if event.button == 1:  # Left mouse button
            x, y = self.component_to_image_space(event.x, event.y)
            closest_index, is_close = self.get_closest_point(x, y)

            if is_close:
                self.dragging_point = closest_index
            else:
                self.point_positions.append((x, y))
            self.canvas_area.queue_draw()

    def on_button_release(self, widget, event):
        self.dragging_point = None

    def on_motion_notify(self, widget, event):
        if self.dragging_point is not None:
            x, y = self.component_to_image_space(event.x, event.y)
            self.point_positions[self.dragging_point] = (x, y)
            self.canvas_area.queue_draw()

    # ... (rest of the code remains unchanged)
