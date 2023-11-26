def get_first_of_month(date, month_offset=0):
    # zero based indexing of month to make math work
    month_count = date.month - 1 + month_offset
    return date.replace(
        day=1, month=month_count % 12 + 1, year=date.year + (month_count // 12)
    )

first_of_next_month = get_first_of_month(today, 1)
