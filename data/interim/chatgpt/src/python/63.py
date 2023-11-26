import asyncio
import contextvars

# Create a new context variable.
my_var = contextvars.ContextVar('my_var')

async def main():
    # Set the context variable.
    my_var.set('Hello, world!')

    # Now, within any function called from main(), 'my_var' can be accessed.
    print(my_var.get())

asyncio.run(main())
