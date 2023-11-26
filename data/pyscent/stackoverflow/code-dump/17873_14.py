#views.py
@csrf_exempt # API doesn't know how to send you csrf token
def check_status(request):
    if request.method == 'POST':
        print(request.POST)# examine the data returned from the API

