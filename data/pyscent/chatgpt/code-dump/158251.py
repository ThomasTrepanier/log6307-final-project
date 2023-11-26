#!/usr/bin/env python3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class Select2DApp(Gtk.Window):
    def __init__(self):
        super(Select2DApp, self).__init__(title="Select Quadrilateral")
        self.set_default_size(800, 600)

        self.image_filename = None
        self.image = None

        self.point_positions = []
        self.dragging_point = None

        self.init_ui()

    def init_ui(self):
        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        self.image_area = Gtk.Image()
        vbox.pack_start(self.image_area, True, True, 0)

        self.canvas_area = Gtk.DrawingArea()
        self.canvas_area.connect("draw", self.on_draw)
        self.canvas_area.add_events(Gdk.EventMask.BUTTON_PRESS_MASK |
                                    Gdk.EventMask.BUTTON_RELEASE_MASK |
                                    Gdk.EventMask.POINTER_MOTION_MASK)
        self.canvas_area.connect("button-press-event", self.on_button_press)
        self.canvas_area.connect("button-release-event", self.on_button_release)
        self.canvas_area.connect("motion-notify-event", self.on_motion_notify)
        vbox.pack_start(self.canvas_area, True, True, 0)

        ok_button = Gtk.Button.new_with_label("OK")
        ok_button.connect("clicked", self.on_ok_button_clicked)
        vbox.pack_start(ok_button, False, False, 0)

    def load_image(self, filename):
        try:
            self.image = GdkPixbuf.Pixbuf.new_from_file(filename)
            self.image_filename = filename
            self.canvas_area.queue_draw()
        except GLib.Error as e:
            print(f"Error loading image: {e}")

    def on_draw(self, area, cr):
        if self.image:
            Gdk.cairo_set_source_pixbuf(cr, self.image, 0, 0)
            cr.paint()

            cr.set_source_rgb(1.0, 0.0, 0.0)
            for x, y in self.point_positions:
                cr.arc(x, y, 5, 0, 2 * 3.14)
                cr.fill()

    def on_button_press(self, widget, event):
        if event.button == 1:  # Left mouse button
            x, y = event.x, event.y
            self.dragging_point = self.get_closest_point(x, y)
            if self.dragging_point is None:
                self.point_positions.append((x, y))
            self.canvas_area.queue_draw()

    def on_button_release(self, widget, event):
        self.dragging_point = None

    def on_motion_notify(self, widget, event):
        if self.dragging_point is not None:
            self.point_positions[self.dragging_point] = (event.x, event.y)
            self.canvas_area.queue_draw()

    def on_ok_button_clicked(self, widget):
        if len(self.point_positions) == 4:
            print("Quadrilateral Points:")
            for x, y in self.point_positions:
                print(f"{x}, {y}")
            Gtk.main_quit()
        else:
            print("Please select four points to form a quadrilateral.")

    def get_closest_point(self, x, y):
        for i, (px, py) in enumerate(self.point_positions):
            if (px - x) ** 2 + (py - y) ** 2 < 25:
                return i
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: select2d <image>")
        sys.exit(1)

    image_filename = sys.argv[1]

    app = Select2DApp()
    app.load_image(image_filename)
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
