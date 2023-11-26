def clean_class_dict(class_dict):
    return_dict = dict(class_dict)
    for key in list(return_dict.keys()):
        if key[0] == "_":
            del return_dict[key]
    return return_dict

def item_in_enum_titles(item: str, enum: Enum):
    enum_dict = clean_class_dict(enum.__dict__)
    if item in enum_dict.keys():
        return True
    else:
        return False
