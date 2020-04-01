import mysql.connector
from typing import Tuple

class DB_Server_Handler:

    def __init__(self, host: str, user: str, 
                passwd: str, database: str):
        ''' Creating Connection to DB '''

        print('\n\nConnecting to {}, please wait a moment...'.format(database))
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
        
        if 'dateday' in pk:
            pk.remove('dateday')
        elif 'DATEDAY' in pk:
            pk.remove('DATEDAY')
        
        return pk

    
    
    def check_data(self, data: str) -> bool:
        ''' Check if the input data is in the local database
            :parram - data : data we´re looking for
            :return - Bool of True/False
        '''

        self.mycursor.execute("show tables")
        myresult = self.mycursor.fetchall()

        check = "a_{}".format(data)

        for element in myresult:
            if check.lower() == element[0].lower() or check.upper() == element[0].upper():
                return True
        else:
            return False
