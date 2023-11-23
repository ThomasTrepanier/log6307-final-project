import os
import pandas as pd

def chunk_text(text, chunk_length, chunk_overlap):
    # Implementation of the chunk_text function from the previous response
    # ...

def process_files_in_folder(folder_path, chunk_length, chunk_overlap):
    file_chunks = []

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

                # Chunk the text using the chunk_text function
                chunks = chunk_text(text, chunk_length, chunk_overlap)

                # Append chunks to the list with corresponding information
                for i, chunk in enumerate(chunks):
                    chunk_id = f"{filename}_chunk_{i + 1}"
                    file_chunks.append({
                        'chunk_id': chunk_id,
                        'chunk_content': chunk,
                        'filename': filename
                    })

    return file_chunks

# Example usage:
folder_path = 'path_to_your_folder'
chunk_length = 200
chunk_overlap = 50

# Process files in the folder and create DataFrame
chunks_data = process_files_in_folder(folder_path, chunk_length, chunk_overlap)
df = pd.DataFrame(chunks_data)

# Display the resulting DataFrame
print(df)
