import math
def llm_calculator(problem):
    # Split the problem into separate terms
    terms = problem.split()
    
    # Initialize result
    result = 0

    # Iterate over each term
    for term in terms:
        # Check if term contains a multiplication operation
        if '*' in term:
            # Split the term into coefficient and variable
            coefficient, variable = term.split('*')
            # Convert coefficient to float
            coefficient = float(coefficient)
            # Check if variable is a valid function in math library
            if variable in dir(math):
                # Add the result of the operation to the total result
                result += coefficient * getattr(math, variable)()
            else:
                raise ValueError(f"Unknown variable: {variable}")
        else:
            # If term does not contain a multiplication operation, treat it as a number
            result += float(term)
    
    # Return the result as a string
    return str(result)
