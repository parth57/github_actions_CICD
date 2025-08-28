from src.maths_op import add, sub


def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(10,15) == 25
    assert add(1,1) == 2
    
def test_sub():
    assert sub(5,3) == 2
    assert sub(-1,1) == -2
    assert sub(2,1) == 1
    assert sub(5,0) == 5