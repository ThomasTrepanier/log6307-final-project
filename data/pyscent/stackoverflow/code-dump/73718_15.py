from typing import Union
    
def convert_decimal(item: Union[dict, list]) -> Union[dict, list]:
    if item is None:
        return None

    elif isinstance(item, list):
        for index, item in enumerate(item):
            if isinstance(item, Decimal):
                item[index] = Decimal128(str(item))
            if isinstance(item, dict):
                convert_decimal(item)
        return item

    elif isinstance(item, dict):
        for k, v in list(item.items()):
            if isinstance(v, dict):
                convert_decimal(v)
            elif isinstance(v, list):
                convert_decimal(v)
            elif isinstance(v, Decimal):
                item[k] = Decimal128(str(v))

        return item
