def lession_group (request):
    results=[]
    parr = list(students.objects.all())
    pick = []
    picked = []
    final = []
    for i in range(4):
        pick = groupp (parr, 2)
        while pick in final or pick[::-1] in final or any(p in picked for p in pick):
            pick = groupp (parr, 2)
        final.append(pick)
        picked.extend(pick)
