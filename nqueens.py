from board import Board
from db_manager import dbConnection
import click
import json

@click.command()
@click.argument('nqueens')
@click.option('--iterative', '-i', is_flag=True,\
help = "Iterate over N and store the solutions in postgres")
@click.option('--solutions', '-s', is_flag=True,\
help = "Print all the N queens solutions stored in postgres")

def main(nqueens, iterative, solutions):
    """
    Application to determinate all the solutions for the N queens problem.
    This application reads the db parameter from the db_settings.json file.
    """
    n = int(nqueens)
    if iterative or solutions:
        with open('db_settings.json') as json_file: #Read the configuration for the db.
            data = json.load(json_file)
            p = data["settings"]
            user = p['user']
            password = p['password']
            host = p['host']
            port = p['port']
            database = p['database']
        DB = dbConnection(user,password,host,port,database)
        if iterative:
            for i in range(1,n+1): #Iterate over N to find the solutions and store the results
                board = Board(i)
                DB.dropTable("queens{}".format(i))
                DB.createTable(i,"queens{}".format(i))
                finds, solutions = board.findSolutions()
                print(finds)
                DB.writeSolutions(solutions)
        else:
            solutions = DB.readSolutions("queens{}".format(n)) # Read the solutions stored in the DB
            if solutions != None:
                for i,queen_solution in enumerate(solutions):
                    print(i+1,"->  ",queen_solution.queen_rows,"  ",queen_solution.queen_cols)
            else:
                print("Table for {0} queens problem not found. \
                    \nRun the application with args. -i {0}  \
                    \nto create this solution's table".format(n))
    else:
        board = Board(n) #Create an object of Board type to find the solution of the n queens problem
        finds, solutions = board.findSolutions()
        solutions = DB.readSolutions("queens8".format(n))
        print(finds)

if __name__ == "__main__":
    main()
