def chunk_text(text, chunk_length, chunk_overlap):
    if chunk_length <= 0 or chunk_overlap < 0 or chunk_overlap >= chunk_length:
        raise ValueError("Invalid parameters. Chunk length should be positive, and overlap should be non-negative and less than the chunk length.")

    chunks = []
    text_length = len(text)
    start = 0

    while start < text_length:
        end = min(start + chunk_length, text_length)
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_length - chunk_overlap

    return chunks

# Example usage:
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu est at ante venenatis varius. Fusce gravida, neque vel aliquam scelerisque, turpis lacus viverra ipsum, a gravida justo elit non elit."
chunk_length = 40
chunk_overlap = 10

chunks = chunk_text(text, chunk_length, chunk_overlap)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")
