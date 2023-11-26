def get_ytplayer_js(html: str) -> Any:
    """Get the YouTube player base JavaScript path.

    :param str html
    The html contents of the watch page.
    :rtype: str
    :returns:
    Path to YouTube's base.js file.
    """
    js_url_patterns = [
        r"\"jsUrl\":\"([^\"]*)\"",
    ]
    for pattern in js_url_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(html)
        if function_match:
            logger.debug("finished regex search, matched: %s", pattern)
            yt_player_js = function_match.group(1)
            return yt_player_js

    raise RegexMatchError(
       caller="get_ytplayer_js", pattern="js_url_patterns"
    )
