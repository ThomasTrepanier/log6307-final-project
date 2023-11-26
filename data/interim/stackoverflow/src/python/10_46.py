def write_pdf_view(request):
    if request.method == 'POST':
       reference = request.POST.get('Reference_IDs') 
       y = Orders.objects.all()
       z = Manifests.objects.all()
       order = y.get(reference=reference)
       manifest = z.filter(reference=reference)
       for manifest_value in manifest:
           print(manifest_value.description)
