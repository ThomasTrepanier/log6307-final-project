def replace_nan(worksheet, row, col, value, format=None):
    if math.isnan(value):
        return worksheet.write_blank(row, col, None, format)
    else:
        return None  # let xlsxwriter do its thing

worksheet.add_write_handler(float, replace_nan)
