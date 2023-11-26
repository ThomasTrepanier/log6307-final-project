# Function to collect messages
def collect_messages(_):
    prompt = inp.value
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response)))
    return pn.pane.Scroll(pn.Column(*panels), width=600, height=400)  # Updated this line

...

dashboard = pn.Column(
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
    inp,
    pn.Row(button_conversation),
    sizing_mode="stretch_both"  # Added this line to make the dashboard expand to available space
)
