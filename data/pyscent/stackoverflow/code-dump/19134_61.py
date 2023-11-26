import pandas as pd
def turn_into_csv(data, csver):
    ids = []
    texts = []
    for each in data:
        texts.append(each["full_text"])
        ids.append(str(each["id"]))

    df = pd.DataFrame({'ID': ids, 'FULL_TEXT': texts})
    writer = pd.ExcelWriter(csver + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', encoding="utf-8-sig")

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
