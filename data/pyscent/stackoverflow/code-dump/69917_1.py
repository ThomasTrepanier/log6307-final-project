import pandas as pd
import numpy as np
import plotly.graph_objs as go

def line(x, y, name):
    return [go.Scatter(x=x, y=y, mode='lines', line=dict(color="rgb(0, 0, 255)"), name=name)]

def line_with_error_band(x, y, y_err, name):
    
    return [
        go.Scatter(x=x, y=y, mode='lines', line=dict(color="rgb(255, 0, 0)"), name=name),
        go.Scatter(x=x, y=y+y_err, mode='lines', line=dict(width=0), showlegend=False),
        go.Scatter(x=x, y=y-y_err, line=dict(width=0), mode='lines', fillcolor="rgba(255, 0, 0, 0.3)", fill='tonexty',
                   showlegend=False)
    ]

# Generate example data
# timeseries y_pred and y_pred_std are starting 5 days later than y_obs 
np.random.seed(42)
x_date = pd.to_datetime(list(range(10)), unit='D', origin=pd.Timestamp('2023-01-01'))
y_obs = np.random.uniform(low=0, high=3, size=10).tolist()
y_pred = np.append(([np.nan] * 5), (y_obs*np.random.uniform(low=0, high=2, size=10))[5:])
y_pred_std = np.append(([np.nan] * 5), [0.1,0.2,0.3, 0.4, 0.5])
df = pd.DataFrame({"x_date" : x_date, "y_obs" : y_obs, "y_pred" : y_pred, "y_pred_std": y_pred_std })

fig = go.Figure()
fig.add_traces(line(df.x_date, df.y_obs, name="observed"))
fig.add_traces(line_with_error_band(df.x_date, df.y_pred, df.y_pred_std, name="predicted"))
