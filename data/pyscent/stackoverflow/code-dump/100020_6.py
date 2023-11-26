"""
I kept your function the same besides removing the invalid conditional branch and adding a 
print statement
"""
def determineGrade (studentScore):
    print("Student earned the following grade: ", end = " ")
    
    if studentScore <= 40:
        print ('F')
    elif studentScore <= 50:
        print ('D')
    elif studentScore <= 60:
        print ('C')
    elif studentScore <= 70:
        print ('B')
    elif studentScore <= 100:
        print ('A')

"""
I kept this function very similar as well except I used a list initialized in main so you have a 
history of all student scores input and how many passed or failed. I also put the fail and passing
variables here for readability and to avoid scope problems.
"""
def determinePass (score_list):
    fail = 0
    passing = 0
    
    for i in range(len(score_list)):
        if score_list[i] <= 40:
            fail += 1
        else:
            passing += 1
            
    print("Students passing: {}".format(passing))
    print("Students failing: {}".format(fail))

"""
I finished this function by using basic list functions that calculate the average. In the future,
use the keyword pass or a stub in your definition if not finished so you can still test it :)
"""
def classAverage (score_list):
    avg = sum(score_list) / len(score_list)
    
    print("Class Average: {}".format(avg))

""" MAIN """
if  __name__ == "__main__":
    # Makes sentinel value known to the user (any negative number).
    print("Welcome. Input a negative integer at any time to exit.")
    # Wrapped input in float() so input only accepts whole and decimal point numbers. 
    studentScore = float(input("Grade for a student: "))
    # Declares an empty list. Remember that they are mutable meaning they can change even in functions.
    score_list = []
    
    # Anything below 0 is considered a sentinel value or what terminates the loop. 
    while studentScore >= 0:
        # If input score is between 0-100:
        if studentScore <= 100:
            # Input score is added to our list for use in the functions.
            score_list.append(studentScore)
            
            determineGrade(studentScore)
            determinePass(score_list)
            classAverage(score_list)
        # If a number beyond 100 is input as a score.
        else:
            print("Invalid. Score must be between 0-100")
        
        # Used to avoid infinite loop and allow as many valid inputs as desired.
        print("Welcome. Input a negative integer at any time to exit.")
        studentScore = float(input("Grade for a student: "))
