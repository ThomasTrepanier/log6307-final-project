"""Test of ENUM"""

from enum import Enum


class ProtocolEnum(Enum):
    """
    ENUM to hold the allowed values for protocol
    """
    HTTP: str = 'http'
    HTTPS: str = 'https'


def try_protocol_enum(protocol: ProtocolEnum) -> None:
    """
    Test of ProtocolEnum
    :rtype: None
    :param protocol: a ProtocolEnum value allows for HTTP or HTTPS only
    :return:
    """
    print(type(protocol))
    print(protocol.value)
    print(protocol.name)


try_protocol_enum(ProtocolEnum.HTTP)

try_protocol_enum('https')
