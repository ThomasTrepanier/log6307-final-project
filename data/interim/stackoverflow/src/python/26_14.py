def Kyletrb(request):
    all = "SELECT Description, Account ,Credit,Debit FROM [Kyle].[dbo].[_btblCbStatement] WHERE Account <> ''"
    cursor.execute(all);
    xAll = cursor.fetchall()
    cursor.close()
    xAll_l = []
    for row in xAll:
        rdict = {}
        rdict["Description"] = row[0]
        rdict["Account"] = row[1]
        rdict["Credit"] = row[2]
        rdict["Debit"] = row[3]
        xAll_l.append(rdict)
    return render(request , 'main/Kyletrb.html' , {"xAlls":xAll_l}) 
