import re
import json

def parse_data(data):
    output = {}

    # Split the data into lines
    lines = data.split("\n")

    # Get and set company info
    output["Company"] = {
        "Full Name": lines[0].strip(),
        "Name": lines[2].strip(),
        "Hiring Status": lines[4].strip()
    }

    # Get and set position info
    position_data = re.match(r'(.*)/(.*) Software Engineer - (.*)', lines[1].strip())
    output["Position"] = {
        "Title": "Software Engineer",
        "Level": position_data.group(2),
        "Type": position_data.group(3)
    }

    # Get and set location info
    location_data = re.match(r'(.*?) \((.*)\)', lines[3].strip())
    output["Location"] = {
        "Country": location_data.group(1),
        "Type": location_data.group(2)
    }

    return json.dumps(output, indent=4)


data = """Ironclad, Inc.
Senior/Staff Software Engineer - AI
Ironclad
United States (Remote)
Actively recruiting
Posted 12h ago"""

print(parse_data(data))
