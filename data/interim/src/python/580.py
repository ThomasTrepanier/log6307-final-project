def generate_abbreviated_highlight(actor, verb, object_):
    return f"{actor} {verb} {object_}."

# Initialize a dictionary to store summarized activities
summarized_activities = {}

# Example list of activities (replace this with your actual activity data)
activities = [
    {"actor": "UserA", "verb": "liked", "object": "your post"},
    {"actor": "UserB", "verb": "liked", "object": "your post"},
    # Add more activities here
]

# Summarize the activities
for activity in activities:
    actor = activity["actor"]
    verb = activity["verb"]
    object_ = activity["object"]
    
    if (actor, verb, object_) in summarized_activities:
        summarized_activities[(actor, verb, object_)] += 1
    else:
        summarized_activities[(actor, verb, object_)] = 1

# Generate and print the summarized highlights
for (actor, verb, object_), count in summarized_activities.items():
    highlight = generate_abbreviated_highlight(actor, verb, object_)
    if count > 1:
        print(f"{highlight} ({count} times)")
    else:
        print(highlight)
