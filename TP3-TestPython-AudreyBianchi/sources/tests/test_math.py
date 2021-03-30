from sources import math

def test_add():
    assert math.add(2, 3) == 5

def test_fibo():
    assert math.fibo(0) == 1
    assert math.fibo(1) == 1
    assert math.fibo(2) == 2
    assert math.fibo(3) == 3
    assert math.fibo(4) == 5    
    assert math.fibo(5) == 8
    assert math.fibo(100) == 573147844013817084101
def test_reverse():
    # Arrange
    greek = ['alpha', 'beta', 'gamma', 'delta']

    # Act
    result = greek.reverse()
    
    # Assert
    assert result is None
    assert greek == ['delta', 'gamma', 'beta', 'alpha']

