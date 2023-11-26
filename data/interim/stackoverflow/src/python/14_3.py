from enum import Enum
from typing import Type, TypeVar, Union

class ProtocolType(Enum):
    HTTP = "http"
    HTTPS = "https"

T = TypeVar("T")

def validate_enum(value: T, enum_type: Type[Enum]) -> T:
    if not any(value == item.value for item in enum_type):
        raise ValueError(f"Invalid value: {value}")
    return value

def my_request(protocol_type: Union[ProtocolType, str], url: str):
    protocol_type = validate_enum(protocol_type, ProtocolType)
    
    print(f"Making a {protocol_type} request to {url}")

# valid calls
my_request("http", "example.com")
my_request("https", "example.com")

# invalid call
my_request("ftp", "example.com")
