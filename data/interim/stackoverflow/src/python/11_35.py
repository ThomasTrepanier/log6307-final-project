def function_to_apply(element):
    return element*2

# Define variables and store them in a container
a,b,c = 1,2,3
container = (a,b,c)

# Apply the function on every element with map
container = tuple(map(function_to_apply, container))
a,b,c = container
