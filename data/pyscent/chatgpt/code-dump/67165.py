@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        alignment = 'text-right' if own_id == user_id else 'text-left'
        with ui.row().classes('w-full'):
            ui.html(f'<div class="chat-message {alignment}">{text}</div>', 
                    css={'background-color': '#f8f8f8', 'padding': '10px', 'border-radius': '5px'})

    # Scroll to bottom of chat messages
    await ui.run_javascript('var element = document.getElementsByClassName("scroll")[0];'
                            'element.scrollTop = element.scrollHeight;', respond=False)
