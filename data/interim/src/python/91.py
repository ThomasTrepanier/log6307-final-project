from pydantic import create_model, Field
from typing import Optional

# JSON schema
schema = {
    "type": "number",
    "title": "Top P",
    "default": 1,
    "maximum": 1,
    "minimum": 0.01,
    "x-order": 3,
    "description": "When decoding text, samples from the top p percentage of most likely tokens; lower to ignore less likely tokens"
}

# Set appropriate Python types based on the schema's type
type_mapping = {
    "number": float,
    "integer": int,
    "string": str,
    "boolean": bool,
    "object": dict,
    "array": list,
}

# Dynamically create the Pydantic model
TopPModel = create_model(
    "TopPModel",
    top_p=(Optional[type_mapping[schema['type']]], Field(
        default=schema.get('default'),
        description=schema.get('description'),
        gt=schema.get('minimum'),
        lt=schema.get('maximum'),
    )),
)

# Now we can use the TopPModel
instance = TopPModel(top_p=0.5)
print(instance)
