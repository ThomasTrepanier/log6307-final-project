def timestamp_to_minutes(timestamp: str) -> int:
    hh, mm = timestamp.split(":")
    return int(hh)*60 + int(mm)

[timestamp_to_minutes(ts) for ts in timestamps]

# Alternative
list(map(timestamp_to_minutes, timestamps))
