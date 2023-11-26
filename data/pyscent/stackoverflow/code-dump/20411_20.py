from django.core.cache import cache

def PageView(request):
    ...
    if request.GET.get('clear') == 'cache':
        if request.user.is_superuser:
            title = request.GET.get('flag') + ' ' + title 
            cache.clear()
    ...
    return render(request, template, context)
