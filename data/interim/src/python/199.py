import yaml

def render_field(value):
    if isinstance(value, list):
        return ', '.join(value)
    return str(value)

with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

header = data['header']
table = "| " + " | ".join(header.values()) + " |\n"
table += "| " + "|".join(["---"] * len(header)) + " |\n"

for entry in data['data']:
    row = "| " + " | ".join(render_field(entry.get(field, '')) for field in header) + " |\n"
    table += row

with open('table.md', 'w') as file:
    file.write(table)
