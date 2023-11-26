from functools import partial

def f(s=None):
    # Define a new function g which takes the current text and takes s
    def g(current_text, s=None):
        if s is not None:
            return current_text + s
        else:
            # If called with an empty argument, just rebind current_text with an extra o
            return partial(g, current_text + "o")

    # Just call g with the initial conditions
    return g("f", s)

print(f()()()()()("s")) # fooooos
print(f("s")) # fs
