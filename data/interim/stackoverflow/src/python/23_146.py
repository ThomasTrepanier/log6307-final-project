def test_it_returns_value_from_question_1():
    s = "2014-01-01 00:12:12"
    candidates = FormatFinder().find_candidate_patterns(s)
    sut = FormatFinder()
    candidates = sut.find_candidate_patterns(s)
    assert "%Y-%m-%d %H:%M:%S" in candidates


def test_it_returns_value_from_question_2():
    s = 'Jan. 04, 2017'
    sut = FormatFinder()
    candidates = sut.find_candidate_patterns(s)
    candidates = list(candidates)
    assert "%b. %d, %Y" in candidates
    assert len(candidates) == 1


def test_it_can_ignore_case():
    # NB: apparently the 'AM/PM' is meant to be capitalised in my locale! 
    # News to me!
    s = "JANUARY 12, 2018 02:12 am"
    sut = FormatFinder(ignore_case=True)
    candidates = sut.find_candidate_patterns(s)
    assert "%B %d, %Y %H:%M %p" in candidates


def test_it_returns_parts_that_have_no_date_component_verbatim():
    # In this string, the 'at' is considered as a 'date' element, 
    # but there is no specifier that produces a candidate for it
    s = "January 12, 2018 at 02:12 AM"
    sut = FormatFinder()
    candidates = sut.find_candidate_patterns(s)
    assert "%B %d, %Y at %H:%M %p" in candidates
