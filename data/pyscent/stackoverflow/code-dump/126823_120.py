def encode_vector(ar):
    return base64.encodestring(ar.tobytes()).decode('ascii')

def decode_vector(ar):
    return np.fromstring(base64.decodestring(bytes(ar.decode('ascii'), 'ascii')), dtype='uint16')
