# Create a new context variable.
my_context_var = contextvars.ContextVar('my_context_var', default=MyContext())

# Somewhere in your task...
my_context = my_context_var.get()
my_context.add_trace('Doing something...')
# Do something, enqueue operation, etc.

# Later...
my_context = my_context_var.get()
trace = my_context.get_trace()
print(trace)  # prints: ['Doing something...']
