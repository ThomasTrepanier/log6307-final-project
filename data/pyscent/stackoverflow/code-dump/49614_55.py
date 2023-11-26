import xlwings as xw
def df_to_excel_util(excel,sheet_to_dataFrame_map):

    with xw.App(visible=False) as app:
        wb = app.books.open(excel)            
        current_sheets = [sheet.name for sheet in wb.sheets]
        
        for sheet_name in sheet_to_dataFrame_map.keys():
            if sheet_name in  current_sheets:
                wb.sheets[sheet_name].delete()
            
            new_sheet = wb.sheets.add(after=wb.sheets.count)
            new_sheet.range('A1').value = sheet_to_dataFrame_map.get(sheet_name)
            new_sheet.name = sheet_name
        wb.save()
