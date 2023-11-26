def vec_dt_replace(series, year=None, month=None, day=None):
    return pd.to_datetime(
        {'year': series.dt.year if year is None else year,
         'month': series.dt.month if month is None else month,
         'day': series.dt.day if day is None else day})
#dfall.date=pd.to_datetime(dfall.date) #(if dfall.date is type string)
dfall.date=vec_dt_replace(dfall.date,day=1)- pd.Timedelta(days=1)
