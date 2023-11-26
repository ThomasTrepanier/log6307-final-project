class Classifier:
    def __init__(self, centroid, threshold: float):
        self.centroid = centroid
        self.threshold: float = threshold

    def predict(self, concepts_pipe):
        predictions = []
        for concept in concepts_pipe:
            predictions.append(self.centroid.similarity(concept) > self.threshold)
        return predictions
