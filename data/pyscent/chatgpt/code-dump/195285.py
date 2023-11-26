import csv

# Load humans' and GPT's answers together (including the "code" column)
def load_chat_data(csv_filename):
    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        text = ""
        for row in reader:
            _, _, entry_text, code = row
            text += entry_text + " " + code + " "
        return text.strip()

# Example usage
csv_filename = "chat_data.csv"
chat_text = load_chat_data(csv_filename)

text = f"""
{chat_text}
"""
