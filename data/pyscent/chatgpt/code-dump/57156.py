@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        alignment = 'justify-end' if user_id == own_id else 'justify-start'
        with ui.row().classes(f'w-full {alignment}'):
            ui.chat_message(text=text, stamp=stamp, avatar=avatar, sent=own_id == user_id)
    # Scroll to bottom of chat messages
    await ui.run_javascript('var element = document.getElementsByClassName("overflow-y-auto")[0];'
                            'element.scrollTop = element.scrollHeight;', respond=False)
