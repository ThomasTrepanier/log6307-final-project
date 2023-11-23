from datetime import datetime
from typing import List, Tuple
from uuid import uuid4

from nicegui import Client, ui

messages: List[Tuple[str, str, str, str]] = []

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

def create_chat_app():
    client = Client()

    def send() -> None:
        stamp = datetime.utcnow().strftime('%X')
        messages.append((user_id, avatar, text.value, stamp))
        text.value = ''
        chat_messages.refresh()

    user_id = str(uuid4())
    avatar = f'https://robohash.org/{user_id}?bgset=bg2'

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    scrollbar_style = r'''
        .scroll::-webkit-scrollbar {
            width: 10px;
        }
        .scroll::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        .scroll::-webkit-scrollbar-thumb {
            background: #888;
        }
        .scroll::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        .scroll {
            overflow-y: scroll;
            padding-right: 10px;  # add right padding to the element
        }
        '''
    ui.add_head_html(f'<style>{anchor_style} {scrollbar_style}</style>')

    chat_app = ui.column().classes('w-full max-w-3xl mx-auto my-6')

    with chat_app:
        with ui.row().classes('w-full no-wrap h-[500px] scroll'):
            with ui.column().classes('w-full items-stretch'):
                chat_messages(user_id)
        with ui.row().classes('w-full no-wrap items-center'):
            with ui.avatar().on('click', lambda: ui.open(main)):
                ui.image(avatar)
            text = ui.input(placeholder='message').on('keydown.enter', send) \
                .props('rounded outlined input-class=mx-3').classes('flex-grow')
        ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
            .classes('text-xs self-end mr-8 m-[-1em] text-primary')

    async def main():
        await client.connect()
        return chat_app

    return main

# Usage
if __name__ == '__main__':
    app = create_chat_app()
    ui.run(app)
