def get_hours(time_duration):
  h, m, s = time_duration.split(':')
  return float(h) + float(m) / 60 + float(s) / 3600

KM_TO_MI_CONVERSION_FACTOR = 1.609344

time_duration = ['0:07:11', '0:15:16', '0:18:17', '0:23:15']
km_distances = ['0.6', '0.4', '1.3', '1.7']
mi_distances = [float(x)/KM_TO_MI_CONVERSION_FACTOR for x in km_distances]
time_in_hours = [get_hours(x) for x in time_duration]
mi_per_hour = [round(x/y, 7) for x, y in zip(mi_distances, time_in_hours)]
km_per_hour = [round(float(x)/y, 7) for x, y in zip(km_distances, time_in_hours)]
print(mi_per_hour) #[3.1140644, 0.9768281, 2.6508817, 2.7260156]
print(km_per_hour) #[5.0116009, 1.5720524, 4.2661805, 4.3870968]
