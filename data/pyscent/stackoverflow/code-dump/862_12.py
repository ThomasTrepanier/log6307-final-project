import dash

from callback_manager import CallbackManager

callback_manager = CallbackManager()


@callback_manager.callback(
    dash.dependencies.Output('label', 'children'),
    [dash.dependencies.Input('call_btn', 'n_clicks')])
def update_label(n_clicks):
    if n_clicks > 0:
        return "Callback called!"
