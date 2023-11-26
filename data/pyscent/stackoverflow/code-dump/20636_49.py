import pandas as pd

def processAndSaveCSV(filename):
  # Read the CSV file
  df = pd.read_csv(filename)

  # Retain only the rows with `ProductOMS` being numeric
  df = df[df['ProductOMS'].str.contains('^\d+')]

  # Save CSV File - Rewrites file
  df.to_csv(filename)
