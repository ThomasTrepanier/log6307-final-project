import inspect

i = [5]  # name "i" refers to an mutable Python list containing immutable integer object 5
print(f'i = {i} (id={id(i)})')  # Note value and ID

# Create function "f" with a parameter whose default is the object
# referred to by name "i" *at this point*.
def f(arg=i):
    print(f'arg = {arg} (id={id(arg)})')

# Use the inspect module to extract the defaults from the function.
# Note the value and ID
defaults = dict(inspect.getmembers(f))['__defaults__']
print(f'defaults = {defaults} (id={id(defaults[0])})')

# name "i" now refers to a different immutable Python integer object of value 6.
i[0] = 6  # MUTATE the content of the object "i" refers to.
print(f'i = {i} (id={id(i)})') # Note value and ID (UNCHANGED!)
f()  # default for function still refers to original list object, but content changed!
i = [7]  # Create a different list object
print(f'i = {i} (id={id(i)})') # Note value and ID (changed)
f(i)     # override the default currently refered to by name "i"
