import sqlalchemy
from sqlalchemy import Column, ARRAY, Integer, orm, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QueenSolution():  #Base class to store the solutions it's mapped to the 'Nqueens' table.
    def __init__(self, queen_rows, queen_cols):
        self.queen_rows = queen_rows
        self.queen_cols = queen_cols

    def __repr__(self):
        return "{} {}".format(self.queen_rows,self.queen_cols)

class dbConnection():
    def __init__(self,user,password,host,port,database): #Creation of the db connection
        self.engine = sqlalchemy.create_engine("postgresql://{}:{}@{}:{}/{}".format(user,password,host,port,database))
        self.metadata = sqlalchemy.MetaData()
        self.metadata.reflect(self.engine)

    def dropTable(self,tablename): #Delete the table to avoid to append records if the application is runned multiple times
        if tablename in self.metadata.tables.keys():
            self.metadata.tables[tablename].drop(self.engine)
            self.metadata.clear()
            self.metadata.reflect(self.engine)

    def createTable(self,n, tablename): #Table creation and mapping with QueenSolution class.
        table_q = Table(tablename, self.metadata,
        Column('id_solution', Integer, primary_key=True),
        Column('queen_rows', ARRAY(Integer)),
        Column('queen_cols', ARRAY(Integer)))
        self.metadata.create_all(self.engine)
        orm.mapper(QueenSolution, table_q)

    def writeSolutions(self, solutions): #Function to store all the solutions in the table 'queensN' from the database.
        session = orm.sessionmaker(self.engine)()
        session.add_all(solutions)
        session.commit()
        orm.clear_mappers()

    def readSolutions(self, tablename): #Function for testing, It's used to verify the DB write operation.
        if tablename in self.metadata.tables.keys():
            table_q = self.metadata.tables[tablename]
            solutions = []
            orm.mapper(QueenSolution, table_q)
            session = orm.sessionmaker(self.engine)()
            for queen_solution in session.query(QueenSolution):
                solutions.append(queen_solution)
            orm.clear_mappers()
            return solutions
        else:
            return None
