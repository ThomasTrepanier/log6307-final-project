def calculate_probability(ranking_difference, k):
    if ranking_difference == 0:
        return 0.5
    elif ranking_difference == -15:
        return 0
    elif ranking_difference > 0:
        return 1 / (1 + k * abs(ranking_difference))
    else:
        return k * abs(ranking_difference) / (1 + k * abs(ranking_difference))

def calculate_matchup_probabilities(ranking, k):
    probabilities = {}
    for team_a in range(1, 17):
        for team_b in range(1, 17):
            if team_a != team_b:
                ranking_difference = team_a - team_b
                probability = calculate_probability(ranking_difference, k)
                losing_probability = 1 - probability
                probabilities[(team_a, team_b)] = (probability, losing_probability)
    return probabilities

# Example usage:
ranking = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
k = 0.5
matchup_probabilities = calculate_matchup_probabilities(ranking, k)
