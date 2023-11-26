Group_A = set(('nice','car','by','shop'))
Group_B = set(('no','thing','great'))

t_string_A = 'there is a car over there'
t_string_B = 'no one is in a car'

set_A = set(t_string_A.split())
set_B = set(t_string_B.split())

def test(string):
    s = set(string.split())
    if Group_A & set_A and Group_B & set_A:
        return 1
    else:
        return 0
