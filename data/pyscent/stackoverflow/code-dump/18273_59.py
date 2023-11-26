def proxy_request(request_type, url, **kwargs):
    req = None  # <------------------------------- Here
    while 1:
        try:
            proxy = get_proxy()
            req = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
            return req
