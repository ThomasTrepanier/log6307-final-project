my_nested_dict = {"global": {"peers": {"15.1.1.1": {"remote_id": "15.1.1.1", "address_family": {"ipv4": {"sent_prefixes": 1, "received_prefixes": 4, "accepted_prefixes": 4}}, "remote_as": 65002, "uptime": 13002, "is_enabled": True, "is_up": True, "description": "== R3 BGP Neighbor ==", "local_as": 65002}}, "router_id": "15.1.1.2"}}
_list = ['peers', 'remote_id', 'remote_as', 'uptime']

def _join(a, b):
  return '{}:{}\n'.format(a, _keys(b, True) if isinstance(b, dict) else b)

def _keys(_d, flag = False):
  return ''.join(_join(a, b) if a in _list else (a+'\n' if flag else '')+_keys(b) 
          for a, b in _d.items())

print(get_keys(my_nested_dict))
