class ResponseCustomMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(ResponseCustomMiddleware, self).__init__(*args, **kwargs)

    def process_template_response(self, request, response):

        if not response.is_rendered and isinstance(response, Response):
            if isinstance(response.data, dict):
                message = response.data.get('message', 'Some error occurred')
                if 'data' not in response.data:
                    response.data = {'data': response.data}
                response.data.setdefault('message', message)
                # you can add you logic for checking in status code is 2** or 4**.
                data_status = 'unknown'
                if response.status_code // 100 == 2:
                    data_status = 'success'
                elif response.status_code // 100 == 4:
                    data_status = 'failure'
                response.data.setdefault('data_status', data_status)
        return response
