def listFairestWeakTeams(ratings):
    current_best_weak_team_rating = -1
    fairest_weak_teams = []
    for weak_team in recursiveWeakTeamGenerator(ratings):
        weak_team_rating = teamRating(weak_team, ratings)
        if weak_team_rating > current_best_weak_team_rating:
            fairest_weak_teams = []
            current_best_weak_team_rating = weak_team_rating
        if weak_team_rating == current_best_weak_team_rating:
            fairest_weak_teams.append(weak_team)
    return fairest_weak_teams


def recursiveWeakTeamGenerator(
    ratings,
    weak_team=[],
    current_applicant_index=0
):
    if not isValidWeakTeam(weak_team, ratings):
        return
    if current_applicant_index == len(ratings):
        yield weak_team
        return
    for new_team in recursiveWeakTeamGenerator(
        ratings,
        weak_team + [current_applicant_index],
        current_applicant_index + 1
    ):
        yield new_team
    for new_team in recursiveWeakTeamGenerator(
        ratings,
        weak_team,
        current_applicant_index + 1
    ):
        yield new_team


def isValidWeakTeam(weak_team, ratings):
    total_rating = sum(ratings)
    weak_team_rating = teamRating(weak_team, ratings)
    optimal_weak_team_rating = total_rating // 2
    if weak_team_rating > optimal_weak_team_rating:
        return False
    elif weak_team_rating * 2 == total_rating:
        # In case of equal strengths, player 0 is assumed
        # to be in the "weak" team
        return 0 in weak_team
    else:
        return True


def teamRating(team_members, ratings):
    return sum(memberRatings(team_members, ratings))    


def memberRatings(team_members, ratings):
    return [ratings[i] for i in team_members]


def getOpposingTeam(team, ratings):
    return [i for i in range(len(ratings)) if i not in team]


ratings = [5, 6, 2, 10, 2, 3, 4]
print("Player ratings:     ", ratings)
print("*" * 40)
for option, weak_team in enumerate(listFairestWeakTeams(ratings)):
    strong_team = getOpposingTeam(weak_team, ratings)
    print("Possible partition", option + 1)
    print("Weak team members:  ", weak_team)
    print("Weak team ratings:  ", memberRatings(weak_team, ratings))
    print("Strong team members:", strong_team)
    print("Strong team ratings:", memberRatings(strong_team, ratings))
    print("*" * 40)
