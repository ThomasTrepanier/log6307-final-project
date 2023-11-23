# Create initial map figure with animation frame
fig_map = px.scatter_mapbox(
    grouped_df,
    lat="Latitude",
    lon="Longitude",
    size="Emissions Intensity Value",
    color="Emissions Intensity Value",
    hover_name="Field Name",
    hover_data=["Year", "gwp", "Emissions Intensity Value"],
    animation_frame="Year",
    color_continuous_scale=px.colors.sequential.Plasma,
    size_max=20,
    zoom=1,
    title="Emissions Intensity by Field"
)
fig_map.update_layout(mapbox_style="open-street-map")

# ... (The rest remains the same)

# Define callback to update bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('map', 'clickData'),
     Input('gwp-dropdown', 'value'),
     Input('metric-dropdown', 'value')]
)
def update_bar_chart(clickData, selected_gwp, selected_metric):
    # Filter data based on selected GWP and metric
    filtered_df = melted_df[(melted_df['gwp'] == selected_gwp) & (melted_df['Emissions Metric'] == selected_metric)]

    # If a field is selected on the map
    if clickData:
        field_name = clickData['points'][0]['hovertext']
        filtered_df = filtered_df[filtered_df['Field Name'] == field_name]

    # Create and return the new bar chart figure without animation frame
    fig_bar = px.bar(
        filtered_df,
        x='Year',
        y='Emissions Intensity Value',
        color='Supply Chain Segment'
    )
    return fig_bar
