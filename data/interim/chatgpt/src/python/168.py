@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        ui.chat_message(text=text, stamp=stamp, avatar=avatar, sent=own_id == user_id)
    # Scroll to bottom of chat messages
    await ui.run_javascript('''
        var element = document.getElementsByClassName("scroll")[0];
        var isScrolledToBottom = element.scrollHeight - element.clientHeight <= element.scrollTop + 1;
        if (!isScrolledToBottom) {
            element.scrollTop = element.scrollHeight - element.clientHeight;
        }''', respond=False)
