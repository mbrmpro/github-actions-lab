def addition(a, b):
    return a + b


def test_addition():
    assert addition(2, 4) == 6


def subtraction(a, b):

    return a - b


def test_subtraction():

    assert subtraction(10, 4) == 6


def multiplication(a, b):

    return a * b


def test_multiplication():

    assert multiplication(3, 5) == 15


def test_text():

    message = "Machine Learning"

    assert message == "Machine Learning"
