from board import Board
from db_manager import dbConnection
import click
import json

@click.command()
@click.argument('nqueens')
@click.option('--iterative', '-i', is_flag=True,\
help = "Iterate over N and store the solutions in postgres")
def main(nqueens,iterative):
    """
    Application to determinate all the solutions for the N queens problem.
    This application reads the db parameter from the db_settings.json file.
    """
    n = int(nqueens)
    if iterative:
        with open('db_settings.json') as json_file: #Read the configuration for the db.
            data = json.load(json_file)
            p = data["settings"]
            user = p['user']
            password = p['password']
            host = p['host']
            port = p['port']
            database = p['database']
        DB = dbConnection(user,password,host,port,database)
        for i in range(1,n+1): #Iterate over N to find the solutions and store the results
            board = Board(i)
            DB.dropTable("queens{}".format(i))
            DB.createTable(i,"queens{}".format(i))
            finds, solutions = board.findSolutions()
            print(finds)
            DB.wirteSolutions(solutions)
    else:
        board = Board(n) #Create an object of Board type to find the solution of the n queens problem
        finds, solutions = board.findSolutions()
        print(finds)

if __name__ == "__main__":
    main()
