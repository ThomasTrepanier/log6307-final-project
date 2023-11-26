def get_json_location(username=os.getlogin()):
    first = "/Users/"
    last = "/Desktop/data-code/Testdata"
    result = first + username + last
    return result
