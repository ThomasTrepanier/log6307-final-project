import os
import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Chunk text files in a folder and save the results to a Parquet file.')
    parser.add_argument('chunk_length', type=int, help='Length of each chunk')
    parser.add_argument('chunk_overlap', type=int, help='Overlap between consecutive chunks')
    parser.add_argument('folder_path', help='Path to the folder containing text files')
    parser.add_argument('output_file', help='Path to the output Parquet file')
    args = parser.parse_args()

    chunk_length = args.chunk_length
    chunk_overlap = args.chunk_overlap
    folder_path = args.folder_path

    # Process files in the folder and create DataFrame
    chunks_data = process_files_in_folder(folder_path, chunk_length, chunk_overlap)
    df = pd.DataFrame(chunks_data)

    # Save the DataFrame to a Parquet file
    output_file_path = args.output_file
    df.to_parquet(output_file_path, index=False)

    print("Chunking completed. Data saved to:", output_file_path)

if __name__ == "__main__":
    main()
