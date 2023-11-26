import csv

# Load only humans' text (excluding GPT's answers)
def load_human_text(csv_filename):
    with open(csv_filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        text = ""
        for row in reader:
            is_human, _, entry_text, _ = row
            if is_human == "True":
                text += entry_text + " "
        return text.strip()

# Example usage
csv_filename = "chat_data.csv"
humans_text = load_human_text(csv_filename)

text = f"""
{humans_text}
"""
