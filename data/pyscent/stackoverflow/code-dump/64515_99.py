def is_action(obj):
    try:
        Action(obj)
    except ValueError:
        return False
    return True
