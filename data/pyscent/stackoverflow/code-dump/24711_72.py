class ActiveLearner:
    def __init__(
        self,
        concepts,
        concepts_similarity,
        max_steps: int,
        samples: int,
        step: float = 0.05,
        change_multiplier: float = 0.7,
    ):
        sorting_indices = np.argsort(-concepts_similarity)
        self.concepts = concepts[sorting_indices]
        self.concepts_similarity = concepts_similarity[sorting_indices]

        self.max_steps: int = max_steps
        self.samples: int = samples
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
