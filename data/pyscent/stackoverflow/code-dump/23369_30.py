def test_repeating_pattern(lst, pat):
    pat_len = len(pat)
    assert len(lst) % pat_len == 0, 'mismatched length of list'
    assert list(pat) * (len(lst) // pat_len) == lst, 'the list does not follow the correct pattern'
    print(lst, 'is valid')


L = ['a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b']
L_broken = ['a','b','b','a','a','b','a','b','a','a','a','b','a','b','b','a']
