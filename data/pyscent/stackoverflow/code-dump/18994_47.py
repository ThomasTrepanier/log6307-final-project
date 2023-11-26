def get_pdf_searchable_pages(fname):
    """ intentifying a digitally created pdf or a scanned pdf"""    
    from pdfminer.pdfpage import PDFPage
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0
    with open(fname, 'rb') as infile:

        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                searchable_pages.append(page_num)
            else:
                non_searchable_pages.append(page_num)
    if page_num == len(searchable_pages):
        return("searchable_pages")
    elif page_num != len(searchable_pages):
        return("non_searchable_pages")
    else:
        return("Not a valid document")
