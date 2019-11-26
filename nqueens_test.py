import pytest

@pytest.fixture
def board_instance():
    import board
    return [board.Board(i) for i in range(8,16)] #Create Boards with i number of queens and size ixi

@pytest.fixture
def database_instance():
    from db_manager import dbConnection
    import json
    with open('db_settings.json') as json_file: #Read the configuration for the db.
        data = json.load(json_file)
        p = data["settings"]
        user = p['user']
        password = p['password']
        host = p['host']
        port = p['port']
        database = p['database']
    DB = dbConnection(user,password,"localhost",port,database)
    return DB

def test_8queen_findSolutions(board_instance):
    finds, solutions = board_instance[0].findSolutions() # First instance is 8 queens board -> Board(8)
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

# This test takes more than 10 min.
#def test_15queen_findSolutions(board_instance):
#    finds, solutions = board_instance[7].findSolutions()
#    assert finds == 2279184

def test_db_writing(board_instance, database_instance): # Compare the DB results with the results given by the function
    database_instance.dropTable("testingTable" )
    database_instance.createTable(8,"testingTable")     # For this test case the Board has 8 queens and size 8x8
    finds, solutions = board_instance[0].findSolutions()
    database_instance.writeSolutions(solutions)
    finds, solutions = board_instance[0].findSolutions()
    database_solutions = database_instance.readSolutions("testingTable")
    for i in range(len(database_solutions)): #
        assert solutions[i].queen_cols == database_solutions[i].queen_cols
