def default_call_api(
    name: str,
    fn_args: dict,
    headers: Optional[dict] = None,
    params: Optional[dict] = None,
    **kwargs: Any,
) -> Any:
    method = _name_to_call_map[name]["method"]
    url = _name_to_call_map[name]["url"]
    path_params = fn_args.pop("path_params", {})
    url = _format_url(url, path_params)
    print(f"Making request to {url} with method {method}")
    print(f"Headers: {headers}")
    print(f"Params: {params}")
    if "data" in fn_args and isinstance(fn_args["data"], dict):
        fn_args["data"] = json.dumps(fn_args["data"])
    _kwargs = {**fn_args, **kwargs}

    # Update the 'params' key with the URL, rather than replacing the entire _kwargs dictionary
    _kwargs['params'] = {'url': 'https://eforms.com/download/2018/01/Non-Disclosure-Agreement-Template.pdf'}

    print(f"Other arguments: {_kwargs}")
    if headers is not None:
        if "headers" in _kwargs:
            _kwargs["headers"].update(headers)
        else:
            _kwargs["headers"] = headers
    if params is not None:
        if "params" in _kwargs:
            _kwargs["params"].update(params)
        else:
            _kwargs["params"] = params
    return requests.request(method, url, **_kwargs)
