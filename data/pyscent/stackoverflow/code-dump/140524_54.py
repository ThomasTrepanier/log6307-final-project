def get_time_of_year(dt, type = 'hours_of_year'):
  intitial_date = datetime(dt.year, 1,1, 00, 00, 00) 
  duration = dt - intitial_date

  days, seconds = duration.days, duration.seconds
  hours = days * 24 + seconds // 3600
  minutes = (seconds % 3600) // 60

  if type == 'hours_of_year':
    return hours
  if type == 'days_of_year':
    return days
  if type == 'seconds_of_year':
    return seconds
  if type == 'minuts_of_year':
    return minutes
