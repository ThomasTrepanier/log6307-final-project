from flask import Flask, Response
from textwrap import dedent

class LiveReload:
    def __init__(self, app: Flask = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.after_request(self.after_request)

    def after_request(self, response: Response):
        if response.status_code != 200:
            return response

        mimetype = response.mimetype or ""
        if not mimetype.startswith("text/html"):
            return response

        if not isinstance(response.response, list):
            return response

        body = b"".join(response.response).decode()
        tag = self.make_tag()
        body = body.replace("</head>", f"{tag}\n</head>")
        response.response = [body.encode("utf8")]
        response.content_length = len(response.response[0])
        return response

    def make_tag(self):
        return dedent("""
            <script>
              document.write('<script src="http://' + (location.host || 'localhost').split(':')[0] +
              ':35729/livereload.js?snipver=1"></' + 'script>')
            </script>
        """).strip()
