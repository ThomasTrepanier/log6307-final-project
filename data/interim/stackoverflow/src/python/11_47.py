def home(request):
   if request.method == 'GET':

       form = DeadlineForm(request.GET)
       if form.is_valid():
           userinput = form.cleaned_data['date']

           birthday = datetime.datetime.strptime(userinput, '%m/%d/%Y').date()
