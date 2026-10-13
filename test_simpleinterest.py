from simpleinterest import Simint

def test_simpleint_pos():
    assert Simint(20000, 8, 12) == 19200

def test_simpleint_zero():
    assert Simint(10000, 7, 0) == 0