class User:
    name = None
    id = None
    dob = None

    def __init__(self, id):
        self.id = id

    def map_dict(self, user_info):
        for k, v in user_info.items():
            setattr(self, k, v)

