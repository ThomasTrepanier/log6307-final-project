import re
import json

def parse_data(data):
    # Split the data into individual job postings
    postings = data.strip().split("\n\n")

    output = []

    for posting in postings:
        posting_dict = {}
        # Split the posting into lines
        lines = posting.split("\n")

        # Get and set company info
        posting_dict["Company"] = {
            "Full Name": lines[0].strip(),
            "Name": lines[2].strip(),
            "Hiring Status": lines[4].strip() if "recruiting" in lines[4] else "Not specified"
        }

        # Get and set position info
        position_data = re.match(r'(.*) (?:Software Engineer|Engineer) -? ?(.*)?', lines[1].strip())
        posting_dict["Position"] = {
            "Title": "Software Engineer" if "Software Engineer" in lines[1] else "Engineer",
            "Level": position_data.group(1),
            "Type": position_data.group(2) if position_data.group(2) else "Not specified"
        }

        # Get and set location info
        location_data = re.match(r'(.*?) \((.*)\)', lines[3].strip())
        posting_dict["Location"] = {
            "Country": location_data.group(1),
            "Type": location_data.group(2)
        }

        output.append(posting_dict)

    return json.dumps(output, indent=4)


data = """Apprentice.io
Senior Full Stack Engineer
Apprentice.io
United States (Remote)
Posted 2mo ago

Thatgamecompany LLC
Full Stack Engineer
thatgamecompany
United States (Remote)
Posted 2mo ago

Path
Senior Software Engineer - Full Stack (Remote)
Path
United States (Remote)
Actively recruiting
Posted 1w ago

Liftoff Mobile
Senior Staff Engineer - Backend, Liftoff Influence
Liftoff Mobile
United States (Remote)
Actively recruiting
Posted 1w ago"""

print(parse_data(data))
