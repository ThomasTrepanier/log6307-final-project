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

    # Add a horizontal box for the checkbox and Confirm button
    hbox = Gtk.HBox(spacing=12)
    hbox.set_margin_top(12)
    hbox.set_margin_bottom(12)
    hbox.set_margin_start(12)  # Add margin on the left side of the hbox
    hbox.set_margin_end(12)    # Add margin on the right side of the hbox
    vbox.pack_start(hbox, False, False, 0)

    # Add the checkbox for snapping
    self.snap_checkbox = Gtk.CheckButton.new_with_label("Snapping")
    hbox.pack_start(self.snap_checkbox, False, False, 0)

    # Add the Confirm button with more padding and a primary style class
    confirm_button = Gtk.Button.new_with_label("Confirm")
    confirm_button.get_style_context().add_class(Gtk.STYLE_CLASS_PRIMARY)
    confirm_button.set_margin_start(6)  # Add padding on the left side of the button
    confirm_button.set_margin_end(6)    # Add padding on the right side of the button
    confirm_button.set_margin_top(6)    # Add padding to the top of the button
    confirm_button.set_margin_bottom(6) # Add padding to the bottom of the button
    confirm_button.connect("clicked", self.on_ok_button_clicked)
    hbox.pack_end(confirm_button, False, False, 0)
