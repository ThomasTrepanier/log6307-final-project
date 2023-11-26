def sigmoid_ranking_probabilities(rank1, rank2):
    """
    Calculates the winning probabilities between two teams based on their rankings, using a sigmoidal function.

    The sigmoid_ranking_probabilities function calculates the probabilities of a team with ranking rank1 winning
    a matchup against a team with ranking rank2. The winning probabilities are determined by a sigmoidal curve,
    where the probabilities gradually transition from low to high values as the ranking difference increases.

    The sigmoidal curve exhibits a rounded shape, resulting in a more gradual change in probabilities for smaller
    ranking differences and a steeper change for larger differences. The curve ensures that the probabilities are
    bounded between 0 and 1.

    Parameters:
        rank1 (int): The ranking of the first team.
        rank2 (int): The ranking of the second team.

    Returns:
        Tuple[float, float]: A tuple containing the winning probability of the first team and the winning probability
        of the second team. The winning probabilities sum up to 1.

    Example:
        >>> sigmoid_ranking_probabilities(5, 10)
        (0.574442516811659, 0.425557483188341)
    """
    # Function implementation here
    pass
