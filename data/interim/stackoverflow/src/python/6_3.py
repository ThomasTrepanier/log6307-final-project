import datetime
from datetime import timedelta

df = pd.DataFrame({"date":['2020-02-04','2020-03-03','2020-04-02','2020-05-05','2020-06-03','2020-07-02'],
                  "month": [1,2,3,4,5,6]})

# Conert to data
def change_time_format(series):
    return datetime.datetime.strptime(series,"%Y-%m-%d")

df.date = df.date.apply(change_time_format)

dates = list(df.date)
previous_m_last_date = []
for d in dates:
    days = d.day
    u_date = d - timedelta(days)
    previous_m_last_date.append(u_date)

df["updated_date"] = previous_m_last_date
df
