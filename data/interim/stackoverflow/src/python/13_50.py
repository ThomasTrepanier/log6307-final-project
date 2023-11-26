grade_checker = {
    96.5: 5.83,
    92.5: 5.5,
    89.5: 5.16,
    86.5: 4.83,
    82.5: 4.5,
    79.5: 4.16,
    76.5: 3.83,
    72.5: 3.5,
    69.5: 3.16,
    68.5: 2.83,
    64.5: 2.5
}

def check_grade(grade):
    for k in grade_checker:
        if grade >= k:
            return grade_checker[k]
    return 0
