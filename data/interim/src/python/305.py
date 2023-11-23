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

    # Add a horizontal box for the checkbox and OK button
    hbox = Gtk.HBox(spacing=6)
    vbox.pack_start(hbox, False, False, 0)

    # Add the checkbox for snapping
    self.snap_checkbox = Gtk.CheckButton.new_with_label("Snap to Points")
    self.snap_checkbox.connect("toggled", self.on_snap_toggled)
    hbox.pack_start(self.snap_checkbox, False, False, 0)

    # Add the OK button
    ok_button = Gtk.Button.new_with_label("OK")
    ok_button.connect("clicked", self.on_ok_button_clicked)
    hbox.pack_end(ok_button, False, False, 0)
