# function to close a workbook given name
def close_wb(wbname):
    import xlwings as xw    
    try: 
        app = xw.apps.active # get the active Excel application
        print ('closing workbook',wbname)
        # make workbook with given name active
        wb = app.books[wbname]
        wb.close()
    except: pass
