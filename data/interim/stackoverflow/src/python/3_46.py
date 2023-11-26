def combine_encoders(*encs):
    def combined(obj):
        for enc in encs:
            try:
                return enc(obj)
            except TypeError:
                pass
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    return combined

combined_encoders = combine_encoders(encode_complex, encode_path)
encoded = json.dumps(data, default=combined_encoders)
