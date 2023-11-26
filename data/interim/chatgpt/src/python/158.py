@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        with ui.row().classes('w-full items-center'):
            alignment = 'justify-end' if user_id == own_id else 'justify-start'
            with ui.row().classes(f'{alignment}'):
                with ui.column().classes('items-start'):
                    with ui.row().classes('items-center'):
                        ui.image(avatar).classes('w-8 h-8')  # w-8 and h-8 control the width and height of the image
                        ui.label(text)
                    ui.label(stamp).classes('text-xs text-gray-400')
    await ui.run_javascript('var element = document.getElementsByClassName("overflow-y-auto")[0];'
                            'element.scrollTop = element.scrollHeight;', respond=False)