def dynamicProgrammingActivitySelection(activities):
    if len(activities) == 0:
        return []

    # Sort activities by finish time
    activities.sort(key=lambda x: x[1])

    # Memoization table
    memo = {}

    def recursive_activity_selection(i):
        # If result exists in memo, return it
        if i in memo:
            return memo[i]

        # Base case
        if i == 0:
            return [activities[0]]

        # Find the last compatible activity
        j = i - 1
        while j >= 0 and activities[j][1] > activities[i][0]:
            j -= 1

        # Include current activity and recurse with last compatible
        include_current = recursive_activity_selection(j) + [activities[i]]
        # Exclude current activity and recurse with previous
        exclude_current = recursive_activity_selection(i - 1)

        # Choose the option that includes more activities
        if len(include_current) > len(exclude_current):
            memo[i] = include_current
        else:
            memo[i] = exclude_current

        return memo[i]

    return recursive_activity_selection(len(activities) - 1)

activities = [[1, 2], [3, 4], [5, 6]]
solution = dynamicProgrammingActivitySelection(activities)
print(f"Solution has {len(solution)} activities:")
for i in solution:
    print(i, end=" ")
