import json
import typing

import numpy as np
import spacy


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


class ActiveLearner:
    def __init__(
        self,
        concepts,
        concepts_similarity,
        samples: int,
        max_steps: int,
        step: float = 0.05,
        change_multiplier: float = 0.7,
    ):
        sorting_indices = np.argsort(-concepts_similarity)
        self.concepts = concepts[sorting_indices]
        self.concepts_similarity = concepts_similarity[sorting_indices]

        self.samples: int = samples
        self.max_steps: int = max_steps
        self.step: float = step
        self.change_multiplier: float = change_multiplier

        # We don't have to ask experts for the same concepts
        self._checked_concepts: typing.Set[int] = set()
        # Minimum similarity between vectors is -1
        self._min_threshold: float = -1
        # Maximum similarity between vectors is 1
        self._max_threshold: float = 1

        # Let's start from the highest similarity to ensure minimum amount of steps
        self.threshold_: float = 1

    def _ask_expert(self, available_concepts_indices):
        # Get random concepts (the ones above the threshold)
        concepts_to_show = set(
            np.random.choice(
                available_concepts_indices, len(available_concepts_indices)
            ).tolist()
        )
        # Remove those already presented to an expert
        concepts_to_show = concepts_to_show - self._checked_concepts
        self._checked_concepts.update(concepts_to_show)
        # Print message for an expert and concepts to be classified
        if concepts_to_show:
            print("\nAre those concepts related to medicine?\n")
            print(
                "\n".join(
                    f"{i}. {concept}"
                    for i, concept in enumerate(
                        self.concepts[list(concepts_to_show)[: self.samples]]
                    )
                ),
                "\n",
            )
            return input("[y]es / [n]o / [any]quit ")
        return "y"

    # True - keep asking, False - stop the algorithm
    def _parse_expert_decision(self, decision) -> bool:
        if decision.lower() == "y":
            # You can't go higher as current threshold is related to medicine
            self._max_threshold = self.threshold_
            if self.threshold_ - self.step < self._min_threshold:
                return False
            # Lower the threshold
            self.threshold_ -= self.step
            return True
        if decision.lower() == "n":
            # You can't got lower than this, as current threshold is not related to medicine already
            self._min_threshold = self.threshold_
            # Multiply threshold to pinpoint exact spot
            self.step *= self.change_multiplier
            if self.threshold_ + self.step < self._max_threshold:
                return False
            # Lower the threshold
            self.threshold_ += self.step
            return True
        return False

    def fit(self):
        for _ in range(self.max_steps):
            available_concepts_indices = np.nonzero(
                self.concepts_similarity >= self.threshold_
            )[0]
            if available_concepts_indices.size != 0:
                decision = self._ask_expert(available_concepts_indices)
                if not self._parse_expert_decision(decision):
                    break
            else:
                self.threshold_ -= self.step
        return self


class Classifier:
    def __init__(self, centroid, threshold: float):
        self.centroid = centroid
        self.threshold: float = threshold

    def predict(self, concepts_pipe):
        predictions = []
        for concept in concepts_pipe:
            predictions.append(self.centroid.similarity(concept) > self.threshold)
        return predictions


if __name__ == "__main__":
    nlp = spacy.load("en_vectors_web_lg")

    centroid = nlp("medicine")

    concepts = json.load(open("concepts_new.txt"))
    concepts_similarity = Similarity(centroid, nlp, n_threads=-1, batch_size=4096)(
        concepts
    )

    learner = ActiveLearner(
        np.array(concepts), concepts_similarity, samples=20, max_steps=50
    ).fit()
    print(f"Found threshold {learner.threshold_}\n")

    classifier = Classifier(centroid, learner.threshold_)
    pipe = nlp.pipe(concepts, n_threads=-1, batch_size=4096)
    predictions = classifier.predict(pipe)
    print(
        "\n".join(
            f"{concept}: {label}"
            for concept, label in zip(concepts[20:40], predictions[20:40])
        )
    )
