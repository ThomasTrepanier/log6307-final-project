def print_event_for(min_, max_):
    reminder = min_ % 2
    for i in range(min_+reminder, max_+reminder, 2):
        print(i)

print_event_for(5, 12)
