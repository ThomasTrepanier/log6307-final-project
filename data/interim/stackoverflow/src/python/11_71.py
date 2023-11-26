class Similarity:
    def __init__(self, centroid, nlp, n_threads: int, batch_size: int):
        # In our case it will be medicine
        self.centroid = centroid

        # spaCy's Language model (english), which will be used to return similarity to
        # centroid of each concept
        self.nlp = nlp
        self.n_threads: int = n_threads
        self.batch_size: int = batch_size

        self.missing: typing.List[int] = []

    def __call__(self, concepts):
        concepts_similarity = []
        # nlp.pipe is faster for many documents and can work in parallel (not blocked by GIL)
        for i, concept in enumerate(
            self.nlp.pipe(
                concepts, n_threads=self.n_threads, batch_size=self.batch_size
            )
        ):
            if concept.has_vector:
                concepts_similarity.append(self.centroid.similarity(concept))
            else:
                # If document has no vector, it's assumed to be totally dissimilar to centroid
                concepts_similarity.append(-1)
                self.missing.append(i)

        return np.array(concepts_similarity)
