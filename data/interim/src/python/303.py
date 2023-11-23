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
