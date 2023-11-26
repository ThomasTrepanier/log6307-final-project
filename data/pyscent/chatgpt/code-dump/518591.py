from anvil import *

class LineForm(Form):

    def __init__(self, **properties):
        # Initialize components
        self.txt_people = TextBox()
        self.txt_time_taken = TextBox()
        self.txt_current_people = TextBox()
        self.btn_store_data = Button(text="Store Data")
        self.btn_estimate_time = Button(text="Estimate Time")
        self.lbl_estimate = Label()

        # Set up event handlers
        self.btn_store_data.set_event_handler('click', self.btn_store_data_click)
        self.btn_estimate_time.set_event_handler('click', self.btn_estimate_time_click)

        # Add components to form
        self.add_component(self.txt_people)
        self.add_component(self.txt_time_taken)
        self.add_component(self.txt_current_people)
        self.add_component(self.btn_store_data)
        self.add_component(self.btn_estimate_time)
        self.add_component(self.lbl_estimate)

    def btn_store_data_click(self, **event_args):
        people = int(self.txt_people.text)
        time_taken = int(self.txt_time_taken.text)
        result = anvil.server.call('store_line_data', people, time_taken)
        alert(result)

    def btn_estimate_time_click(self, **event_args):
        current_people = int(self.txt_current_people.text)
        estimated_time = anvil.server.call('estimate_line_time', current_people)
        self.lbl_estimate.text = estimated_time
