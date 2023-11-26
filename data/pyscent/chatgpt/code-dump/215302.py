def checkerboard(latitudes, longitudes):
    # Convert degrees to radians as numpy trig functions expect radians
    latitudes_rad = np.deg2rad(latitudes)
    longitudes_rad = np.deg2rad(longitudes)

    # Convert latitudes and longitudes to a square size scale
    latitudes_scaled = np.floor(latitudes_rad / np.deg2rad(params.square_size))
    longitudes_scaled = np.floor(longitudes_rad / np.deg2rad(params.square_size))

    # Create the checkerboard pattern
    return (latitudes_scaled + longitudes_scaled) % 2
