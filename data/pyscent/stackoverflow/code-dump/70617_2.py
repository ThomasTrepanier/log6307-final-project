from Soft.SoftWork.manModules import *
# no change to import statement but need to add Soft to PYTHONPATH

def foo():
    print("called foo in man1.py")
    print("foo call module1 from manModules: " + module1())
