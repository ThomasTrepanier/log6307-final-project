from IPython.core.magic import register_line_magic
import subprocess

@register_line_magic
def run_local_server(line):
    handle = IPython.display.display(
            IPython.display.Pretty("Launching my server..."),
            display_id=True,
    )
    subprocess.Popen(['python', '-m', 'http.server'])
    shell = """
        (async () => {
            const url = new URL(await google.colab.kernel.proxyPort(8000, {'cache': true}));
            const iframe = document.createElement('iframe');
            iframe.src = url;
            iframe.setAttribute('width', '100%');
            iframe.setAttribute('height', '400');
            iframe.setAttribute('frameborder', 0);
            document.body.appendChild(iframe);
        })();
    """
    script = IPython.display.Javascript(shell)
    handle.update(script)
