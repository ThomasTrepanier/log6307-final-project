def line(x, y, name):
    return [go.Scatter(x=x, y=y, mode='lines', line=dict(color="rgb(0, 0, 255)"), name=name)]

def line_with_error_band(x, y, y_err, name):
    
    return [
        go.Scatter(x=x, y=y, mode='lines', line=dict(color="rgb(255, 0, 0)"), name=name),
        go.Scatter(x=x, y=y+y_err, mode='lines', line=dict(width=0), showlegend=False),
        go.Scatter(x=x, y=y-y_err, line=dict(width=0), mode='lines', fillcolor="rgba(255, 0, 0, 0.3)", fill='tonexty',
                   showlegend=False)
    ]
