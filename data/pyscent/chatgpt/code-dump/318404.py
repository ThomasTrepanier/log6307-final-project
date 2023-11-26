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

def load_hnsw_index(index_file):
    # Load the HNSW index from the specified file
    index = hnswlib.Index(space='cosine', dim=0)
    index.load_index(index_file)

    return index

def create_query_embedding(query, model):
    # Encode the query to get its embedding
    embedding = model.encode([query])[0]

    return embedding

def find_nearest_neighbors(index, query_embedding, k=5):
    # Find the k-nearest neighbors for the query embedding
    labels, distances = index.knn_query(query_embedding, k=k)

    return labels, distances

def main():
    parser = argparse.ArgumentParser(description='Script to create and use an HNSW index for similarity search.')
    parser.add_argument('input_file', help='Input file containing text chunks in a Parquet format')
    parser.add_argument('output_file', help='Output file to save the HNSW index with .bin extension')
    parser.add_argument('--query', help='Query text for similarity search')
    parser.add_argument('--k', type=int, default=5, help='Number of nearest neighbors to retrieve')
    args = parser.parse_args()

    # Read the input Parquet file and create embeddings
    df = pd.read_parquet(args.input_file)
    embeddings = get_sentence_embeddings(df['chunk_content'].tolist())

    # Create the HNSW index and save it
    index = create_hnsw_index(embeddings)
    index.save_index(args.output_file)

    print("HNSW index created and saved successfully!")

    if args.query:
        # Load the HNSW index from the file
        loaded_index = load_hnsw_index(args.output_file)

        # Create an embedding for the query
        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        query_embedding = create_query_embedding(args.query, model)

        # Find the k-nearest neighbors for the query
        labels, distances = find_nearest_neighbors(loaded_index, query_embedding, k=args.k)

        # Print the results
        print(f"Query: {args.query}")
        for i, label in enumerate(labels[0]):
            print(f"Nearest Neighbor {i+1}:")
            print(f"Chunk ID: {df['chunk_id'][label]}")
            print(f"Chunk Content: {df['chunk_content'][label]}")
            print(f"Distance: {distances[0][i]}")
            print()

if __name__ == "__main__":
    main()
