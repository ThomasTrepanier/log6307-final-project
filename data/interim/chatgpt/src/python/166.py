@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        alignment = 'text-right' if own_id == user_id else 'text-left'
        ui.html(f'<div class="chat-message {alignment}">{text}</div>')

    # Scroll to bottom of chat messages
    await ui.run_javascript('var element = document.getElementsByClassName("scroll")[0];'
                            'element.scrollTop = element.scrollHeight;', respond=False)


@ui.page('/')
async def main(client: Client):
    def send() -> None:
        stamp = datetime.utcnow().strftime('%X')
        messages.append((user_id, avatar, text.value, stamp))
        text.value = ''
        chat_messages.refresh()

    user_id = str(uuid4())
    avatar = f'https://robohash.org/{user_id}?bgset=bg2'

    styles = """
    <style>
        .chat-message {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 5px;
        }
        .text-right {
            text-align: right;
        }
        .text-left {
            text-align: left;
        }
    </style>
    """
    ui.add_head_html(styles)

    with ui.card().classes('w-full max-w-3xl mx-auto my-6'):
        await client.connected()  # chat_messages(...) uses run_javascript which is only possible after connecting
        with ui.row().classes('w-full max-w-2xl mx-auto h-[500px] overflow-y-auto'):
            with ui.column().classes('items-stretch'):
                await chat_messages(user_id)
        with ui.row().classes('w-full no-wrap items-center'):
            with ui.avatar().on('click', lambda: ui.open(main)):
                ui.image(avatar)
            text = ui.input(placeholder='message').on('keydown.enter', send) \
                .props('rounded outlined input-class=mx-3').classes('flex-grow')
        ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
            .classes('text-xs self-end mr-8 m-[-1em] text-primary')

ui.run()
