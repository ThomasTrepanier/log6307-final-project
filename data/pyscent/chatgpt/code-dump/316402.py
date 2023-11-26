from sentence_transformers import SentenceTransformer

def get_sentence_embeddings(sentences):
    # Load a pre-trained model
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    # Encode the sentences to get their embeddings
    embeddings = model.encode(sentences)

    return embeddings

# Example usage:
sentences = ["I love natural language processing.", "Sentence embeddings are awesome!", "Hello, how are you?"]
embeddings = get_sentence_embeddings(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(f"Sentence: {sentence}")
    print(f"Embedding: {embedding}")
    print()
