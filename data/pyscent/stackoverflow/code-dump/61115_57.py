class Action(Enum):
    NEW_CUSTOMER = 1
    LOGIN = 2
    BLOCK = 3

action = 'new_customer'
try:
    action = Action[action.upper()]
    print("action type exists")
except KeyError:
    print("action type doesn't exists")
