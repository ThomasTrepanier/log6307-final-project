def write_pdf_view(request):
    if request.method == 'POST':
        reference = request.POST.get('Reference_IDs') 
        manifest = Manifests.objects.filter(reference=reference)
        order = Orders.objects.get(reference=reference)
