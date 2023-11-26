class LineForm(LineFormTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)

    def btn_store_data_click(self, **event_args):
        people = int(self.txt_people.text)
        time_taken = int(self.txt_time_taken.text)
        result = anvil.server.call('store_line_data', people, time_taken)
        alert(result)

    def btn_estimate_time_click(self, **event_args):
        current_people = int(self.txt_current_people.text)
        estimated_time = anvil.server.call('estimate_line_time', current_people)
        self.lbl_estimate.text = estimated_time
