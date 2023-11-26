from _ctypes import PyObj_FromPtr
import json
import re


class FloatWrapper(object):
    """ Float value wrapper. """
    def __init__(self, value):
        self.value = value


class MyEncoder(json.JSONEncoder):
    FORMAT_SPEC = '@@{}@@'
    regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))  # regex: r'@@(\d+)@@'

    def default(self, obj):
        return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, FloatWrapper)
                else super(MyEncoder, self).default(obj))

    def iterencode(self, obj, **kwargs):
        for encoded in super(MyEncoder, self).iterencode(obj, **kwargs):
            # Check for marked-up float values (FloatWrapper instances).
            match = self.regex.search(encoded)
            if match:  # Get FloatWrapper instance.
                id = int(match.group(1))
                float_wrapper = PyObj_FromPtr(id)
                json_obj_repr = '%.7f' % float_wrapper.value  # Create alt repr.
                encoded = encoded.replace(
                            '"{}"'.format(self.FORMAT_SPEC.format(id)), json_obj_repr)
            yield encoded


d = dict()
d['val'] = FloatWrapper(5.78686876876089075543)  # Must wrap float values.
d['name'] = 'kjbkjbkj'

with open('float_test.json', 'w') as file:
    json.dump(d, file, cls=MyEncoder, indent=4)
