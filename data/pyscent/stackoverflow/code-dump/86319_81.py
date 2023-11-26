def repfree(s):
    if re.search(r'^.*(.).*\1.*$', s):
        print("True")
    else:
        print("False")
