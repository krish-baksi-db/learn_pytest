from src.simple_maths.simple_maths import sum, difference, average


def test_sum():
    assert sum(1, 0) == 1
    assert sum(0, 1) == 1
    assert sum(0, 0) == 0
    assert sum(5, 4) == 9
    assert sum(4., 5.) == 9.



def test_difference():
    assert difference(1, 0) == 1
    assert difference(0, 1) == -1
    assert difference(0, 0.) == 0.
    assert difference(10, 5.) == 5.


def test_average():
    assert average([1., 1, 2, 2]) == 1.5
    assert average([]) == None
    assert average([1]) == 1
