import simplejson as json
from pymongo import MongoClient
from decimal import Decimal
from bson.decimal128 import Decimal128

def convert_decimal(dict_item):
    # This function iterates a dictionary looking for types of Decimal and converts them to Decimal128
    # Embedded dictionaries and lists are called recursively.
    if dict_item is None: return None

    for k, v in list(dict_item.items()):
        if isinstance(v, dict):
            convert_decimal(v)
        elif isinstance(v, list):
            for l in v:
                convert_decimal(l)
        elif isinstance(v, Decimal):
            dict_item[k] = Decimal128(str(v))

    return dict_item

db = MongoClient()['mydatabase']
json_string = '{"A" : {"B" : [{"C" : {"Horz" : 0.181665435,"Vert" : 0.178799435}}]}}'
json_dict = json.loads(json_string, use_decimal=True)
db.this_collection.insert_one(convert_decimal(json_dict))
print(db.this_collection.find_one())
