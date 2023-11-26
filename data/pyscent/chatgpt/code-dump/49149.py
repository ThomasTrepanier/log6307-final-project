@ui.page('/')
async def main(client: Client):
    def send() -> None:
        stamp = datetime.utcnow().strftime('%X')
        messages.append((user_id, avatar, text.value, stamp))
        text.value = ''
        chat_messages.refresh()

    user_id = str(uuid4())
    avatar = f'https://robohash.org/{user_id}?bgset=bg2'

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    ui.add_head_html(f'<style>{anchor_style}</style>')
    
    with ui.card():
        with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
            with ui.row().classes('w-full no-wrap items-center'):
                with ui.avatar().on('click', lambda: ui.open(main)):
                    ui.image(avatar)
                text = ui.input(placeholder='message').on('keydown.enter', send) \
                    .props('rounded outlined input-class=mx-3').classes('flex-grow')
            ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
                .classes('text-xs self-end mr-8 m-[-1em] text-primary')
        
        await client.connected()  # chat_messages(...) uses run_javascript which is only possible after connecting
        with ui.column().classes('w-full max-w-2xl mx-auto items-stretch'):
            await chat_messages(user_id)
