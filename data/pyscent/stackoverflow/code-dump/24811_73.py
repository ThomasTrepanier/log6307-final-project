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
