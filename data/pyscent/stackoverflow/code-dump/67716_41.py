import moment

def dates_bwn_twodates(start_date, end_date):
    diff = abs(start_date.diff(end_date).days)
    
    for n in range(0,diff+1):
        yield start_date.strftime("%Y-%m-%d")
        start_date = (start_date).add(days=1)

sdate = moment.date('2019-03-22')   #start date
edate = moment.date('2019-04-09')   #end date  
