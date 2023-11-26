@implement_linux(None)
def some_function():
    print('Linux')

@implement_windows(some_function)
def some_function():
   print('Windows')

implement_other_platform = implement_for_os('OtherPlatform')

@implement_other_platform(some_function)
def some_function():
   print('Other platform')

