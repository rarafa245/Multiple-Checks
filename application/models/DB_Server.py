import mysql.connector
from typing import Tuple

class DB_Server_Handler:

    def __init__(self, host: str, user: str, 
                passwd: str, database: str):
        ''' Creating Connection to DB '''

        print('Connecting to {}, please wait a moment...'.format(database))
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        self.mycursor = self.mydb.cursor()
        self.curDB = database
        print('Connection Successful!')
    
    def get_pks(self, table: str) -> Tuple[str]:
        ''' Get the PK´s Elements of the Table 
            :parram - table : str containing the name of the table
            :return - Tuple of Strings with the name of the PK´s
        '''
        
        self.mycursor.execute("DESCRIBE  a_{}".format(table.lower()))
        myresult = self.mycursor.fetchall()
        
        pk = []
        for element in myresult:
            if 'PRI' in element:
                pk.append(element[0])
        
        return pk
    
    def check_data(self, data: str) -> bool:
        ''' Check id the input data is in the table
            :parram - data : data we´re looking for
            :return - Bool of True/False
        '''

        self.mycursor.execute("SELECT tableName FROM  _table_ids")
        myresult = self.mycursor.fetchall()

        for element in myresult:
            if data in element:
                return True
        else:
            return False

    def add_data(self, tableName, tableIDs):

        sql = "INSERT INTO _table_ids (tableName, tableIDs) VALUES (%s, %s)"
        val = (tableName, tableIDs)

        self.mycursor.execute(sql, val)
        self.mydb.commit()

        return (self.mycursor.rowcount, "record inserted.")
    
    
