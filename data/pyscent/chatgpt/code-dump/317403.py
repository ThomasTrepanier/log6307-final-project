import argparse
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import hnswlib

def get_sentence_embeddings(sentences):
    # Load a pre-trained model
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    # Encode the sentences to get their embeddings
    embeddings = model.encode(sentences)

    return embeddings

def create_hnsw_index(embeddings, M=16, efC=100):
    # Create the HNSW index
    num_dim = embeddings.shape[1]
    index = hnswlib.Index(space='cosine', dim=num_dim)
    index.init_index(max_elements=embeddings.shape[0], ef_construction=efC, M=M)
    index.add_items(embeddings)

    return index

def main():
    parser = argparse.ArgumentParser(description='Script to create an HNSW index from text chunks in a Parquet file.')
    parser.add_argument('input_file', help='Input file containing text chunks in a Parquet format')
    parser.add_argument('output_file', help='Output file to save the HNSW index with .bin extension')
    args = parser.parse_args()

    # Read the input Parquet file
    df = pd.read_parquet(args.input_file)

    # Get the embeddings for the text chunks
    embeddings = get_sentence_embeddings(df['chunk_content'].tolist())

    # Create the HNSW index
    index = create_hnsw_index(embeddings)

    # Save the index to the output file
    index.save_index(args.output_file)

    print("HNSW index created and saved successfully!")

if __name__ == "__main__":
    main()
