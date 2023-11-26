def generate_abbreviated_highlight(activity):
    # Parse the activity to extract relevant information
    actor = activity['actor']
    verb = activity['verb']
    object_ = activity['object']
    context = activity.get('context', {})

    # Check if there are any additional actors in the context
    additional_actors = context.get('additionalActors', [])

    # Generate the abbreviated highlight based on the information
    if additional_actors:
        actor_names = [actor['displayName'] for actor in additional_actors]
        actor_names.append(actor['displayName'])
        actor_list = ', '.join(actor_names[:-1]) + ' and ' + actor_names[-1]
        highlight = f"{actor_list} {verb} {object_['displayName']}."
    else:
        highlight = f"{actor['displayName']} {verb} {object_['displayName']}."

    return highlight

# Example activity data (replace this with your actual activity data)
activity_data = {
    "actor": {
        "displayName": "UserA"
    },
    "verb": "liked",
    "object": {
        "displayName": "your post"
    },
    "context": {
        "additionalActors": [
            {"displayName": "userB"},
            {"displayName": "userC"},
            # Add more additional actors if needed
        ]
    }
}

# Generate and print the abbreviated highlight
highlight = generate_abbreviated_highlight(activity_data)
print(highlight)
