def remdup(ar):
    d = {}
    for i, v in enumerate(ar):
        d[v] = i
    return [pair[0] for pair in sorted(d.items(), key=lambda x: x[1])]


if __name__ == "__main__":
    test_case = [3, 1, 3, 5]
    output = remdup(test_case)
    expected_output = [1, 3, 5]
    assert output == expected_output, f"Error in {test_case}"

    test_case = [3, 5, 7, 5, 3, 7, 10]
    output = remdup(test_case)
    expected_output = [5, 3, 7, 10]
    assert output == expected_output, f"Error in {test_case}"
