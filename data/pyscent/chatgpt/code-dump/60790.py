import csv
import math
import argparse

def load_airports(filename):
    # Define the dictionary
    airport_dict = {}

    # Open the file
    with open(filename, 'r') as f:
        # Create a CSV reader
        reader = csv.DictReader(f)
        # Iterate over the rows
        for row in reader:
            # Get the IATA code, latitude, and longitude
            iata_code = row['IATA']
            lat = float(row['lat'])
            lon = float(row['long'])
            # Only keep rows where the IATA code is not empty
            if iata_code:
                airport_dict[iata_code] = (lat, lon)

    return airport_dict

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 

    # Radius of earth in kilometers
    r = 6371
    return c * r

def main():
    parser = argparse.ArgumentParser(description="Calculate the distance between two airports.")
    parser.add_argument('airport1', help="IATA code of the first airport")
    parser.add_argument('airport2', help="IATA code of the second airport")

    args = parser.parse_args()

    airport_dict = load_airports('airports_corrected.csv')

    if args.airport1 in airport_dict and args.airport2 in airport_dict:
        lat1, lon1 = airport_dict[args.airport1]
        lat2, lon2 = airport_dict[args.airport2]
        distance = calculate_distance(lat1, lon1, lat2, lon2)
        print(f"The distance between {args.airport1} and {args.airport2} is {distance} kilometers.")
    else:
        print("One or both IATA codes are not found in the dataset.")

if __name__ == "__main__":
    main()
