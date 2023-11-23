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

def create_chat_with_ai_tab():
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

    chat_with_ai_tab = ui.tab('Chat with AI')

    with chat_with_ai_tab:
        with ui.column():
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

    return chat_with_ai_tab

# Usage
if __name__ == '__main__':
    key_down_handler = KeyDownHandler()

    with ui.row():
        # First column: video stream and robot status
        with ui.column():
            # Video stream row
            with ui.card().tight().style("width: 900px"):
                image = ui.image('http://10.0.0.140:8000/stream.mjpg')

        # Second column: manual controls and chat with AI
        with ui.column():
            with ui.tabs().classes('w-full') as tabs:
                chat_with_ai = create_chat_with_ai_tab()
                manual_controls = ui.tab('Manual Controls')

            with ui.tab_panels(tabs, value=manual_controls).classes('w-full'):
                with ui.tab_panel(manual_controls):
                    # Sliders for everything
                    with ui.card().style("margin-bottom: 10px"):
                        slider = ui.slider(min=0, max=100, value=50).classes("w-1/2")

                    # WASD+QE controls
                    with ui.row():
                        with ui.card():
                            with ui.grid(columns=3).style("gap: 7px"):
                                key_down_handler.on_key_down('Q', lambda: None)
                                key_down_handler.on_key_down('W', lambda: None)
                                key_down_handler.on_key_down('E', lambda: None)
                                key_down_handler.on_key_down('A', lambda: None)
                                key_down_handler.on_key_down('S', lambda: None)
                                key_down_handler.on_key_down('D', lambda: None)
                            ui.markdown("**WASD** - direction\n\n**QE** - step left/right")

                        # Second row: YUIHJK controls
                        with ui.card():
                            with ui.grid(columns=3).style("gap: 7px"):
                                key_down_handler.on_key_down('U', lambda: None)
                                key_down_handler.on_key_down('I', lambda: None)
                                key_down_handler.on_key_down('O', lambda: None)
                                key_down_handler.on_key_down('J', lambda: None)
                                key_down_handler.on_key_down('K', lambda: None)
                                key_down_handler.on_key_down('L', lambda: None)
                            ui.markdown("**JL** - roll, **UO** - yaw,\n\n**IK** - pitch")

    keyboard = ui.keyboard(on_key=key_down_handler.handle_keys)
    keyboard.active = True

    app = create_chat_with_ai_tab()
    ui.run(app)
