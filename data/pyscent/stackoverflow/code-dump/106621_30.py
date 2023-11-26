@app.post('/my-endpoint')
async def my_endpoint(stats: Stats, request: Request):
    x = 'x-forwarded-for'.encode('utf-8')
    for header in request.headers.raw:
        if header[0] == x:
            print("Find out the forwarded-for ip address")
            origin_ip, forward_ip = re.split(', ', header[1].decode('utf-8'))
            print(f"origin_ip:\t{origin_ip}")
            print(f"forward_ip:\t{forward_ip}")
    return {'status': 1, 'message': 'ok'}
