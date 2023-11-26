def get_callbacks(app):
    @app.callback([Output("figure1", "figure")],
                  [Input("child1", "value")])
    def callback1(figure):
        return

    @app.callback([Output("figure2", "figure")],
                  [Input("child2", "value")])
    def callback2(figure):
        return
