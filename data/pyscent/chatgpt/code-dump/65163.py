@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        with ui.row().classes('w-full'):
            ui.chat_message(text=text, stamp=stamp, avatar=avatar, sent=own_id == user_id).classes('items-end' if own_id == user_id else 'items-start')
    # Scroll to bottom of chat messages
    await ui.run_javascript('var element = document.getElementsByClassName("scroll")[0];'
                            'element.scrollTop = element.scrollHeight;', respond=False)
