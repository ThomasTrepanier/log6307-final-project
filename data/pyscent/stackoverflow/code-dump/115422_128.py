@pytest.mark.myskip
def test_skip():
    assert True


@pytest.mark.myskip(1 == 1, reason='my skip')
def test_skipif():
    assert True
