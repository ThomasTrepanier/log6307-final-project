def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name
        

import pandas as pd
import plotly.express as px

d = {'col1': [1, 2, 3], 'col2': [3, 4, 5]}
df = pd.DataFrame(data=d)
fig = px.line(df, x=df.index, y=['col1', 'col2'])
custom_legend_name(['hello','hi'])
fig.show()
