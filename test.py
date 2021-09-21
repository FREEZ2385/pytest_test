def test_case_first():
    assert 1

def function_three_add(num):
    return num + 3

def test_case_second():
    number_data = 1

    expect = 5
    result = function_three_add(number_data)
    assert expect == result