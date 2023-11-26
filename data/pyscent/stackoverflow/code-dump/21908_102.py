def function(arg0, **kwargs):
    print("arg is", arg0, "a is", kwargs["a"], "b is", kwargs["b"])

d = {"a":1, "b":2}
function(0., **d)
