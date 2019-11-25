import pytest

@pytest.fixture
def board_instance():
    import board
    return [board.Board(i) for i in range(8,16)]

def test_8queen_findSolutions(board_instance):
    finds, solutions = board_instance[0].findSolutions()
    assert finds == 92

def test_9queen_findSolutions(board_instance):
    finds, solutions = board_instance[1].findSolutions()
    assert finds == 352

def test_10queen_findSolutions(board_instance):
    finds, solutions = board_instance[2].findSolutions()
    assert finds == 724

def test_11queen_findSolutions(board_instance):
    finds, solutions = board_instance[3].findSolutions()
    assert finds == 2680

def test_12queen_findSolutions(board_instance):
    finds, solutions = board_instance[4].findSolutions()
    assert finds == 14200

def test_13queen_findSolutions(board_instance):
    finds, solutions = board_instance[5].findSolutions()
    assert finds == 73712

def test_14queen_findSolutions(board_instance):
    finds, solutions = board_instance[6].findSolutions()
    assert finds == 365596

#def test_15queen_findSolutions(board_instance):
#    finds, solutions = board_instance[7].findSolutions()
#    assert finds == 2279184
