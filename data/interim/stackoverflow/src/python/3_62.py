def js_url(html: str) -> str:
    """Get the base JavaScript url.

    Construct the base JavaScript url, which contains the decipher
    "transforms".

    :param str html:
        The html contents of the watch page.
    """
    base_js = get_ytplayer_config(html)["assets"]["js"]
    return "https://youtube.com" + base_js
