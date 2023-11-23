@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        ui.column().classes('w-full').classes('items-end' if own_id == user_id else 'items-start') \
            .with_html(html_message(user_id, avatar, text, stamp))
    # Scroll to bottom of chat messages
    await ui.run_javascript('var element = document.getElementsByClassName("scroll")[0];'
                            'element.scrollTop = element.scrollHeight;', respond=False)

...

@ui.page('/')
async def main(client: Client):
    ...
    with ui.row().classes('w-full max-w-2xl mx-auto h-[500px] scroll px-2'):  # change class to "scroll"
        with ui.column().classes('w-full items-stretch'):  # here we add 'w-full'
            await chat_messages(user_id)
    ...
