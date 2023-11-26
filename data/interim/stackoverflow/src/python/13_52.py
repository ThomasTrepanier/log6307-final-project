def grade_checker(grade):

    if grade>=96.5: return 5.83
    elif grade>=92.5: return 5.5
    elif grade>=89.5: return 5.16
    elif grade>=86.5: return 4.83
    elif grade>=82.5: return 4.5
    elif grade>=79.5: return 4.16
    elif grade>=76.5: return 3.83
    elif grade>=72.5: return 3.5
    elif grade>=69.5: return 3.16
    elif grade>=68.5: return 2.83
    elif grade>=64.5: return 2.5
    else: return 0

grade_checker(75)
grade_checker(62)
grade_checker(94)
