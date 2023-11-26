class B:
    value = ''
# You have a single attribute, `B.value`

b1, b2 = B(), B()
b1.value = 'hello'
# This shadows b1's reference to B.value,
# inserting a local reference to its own attribute of the same name.
# You can check this with the id() function

b2.value   # this still refers to the class attribute.
