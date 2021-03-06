import mysql.connector
from application.logging_manager import create_logging_debug

# Creating a Logger
loggin_debug = create_logging_debug(__name__)

class DB_Netchart_Handler:

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

    
    def check_data(self, data: str) -> bool:
        ''' Check if the input data is in the table _tables_ids
            :parram - data : data we´re looking for
            :return - Bool of True/False
        '''

        self.mycursor.execute("SELECT tableName FROM _table_ids_copy")
        myresult = self.mycursor.fetchall()

        for element in myresult:
            if data.lower() in element or data.upper() in element:
                return True
        else:
            return False

    def add_data(self, tableName: str, tableIDs: str) -> None:
        ''' Add one register in _table_ids 
        :parram - tableName : String with name of the table
                - tableIDs : String with pks of the table
        :return - None 
        '''

        sql = "INSERT INTO _table_ids_copy (tableName, tableIDs) VALUES (%s, %s)"
        val = (tableName, tableIDs)

        # Adding Infos in Logger
        loggin_debug.debug('''
            Table: {},
            PKs: {}'''.format(
             tableName, tableIDs
         ))

        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        except:
            error_message = 'Error! Table not registed! Check the connection or the host'
            print(error_message)

            # Adding Error Message Info in Logger
            loggin_debug.debug(error_message)
            return

        success_msg = self.mycursor.rowcount, "record inserted."
        print(success_msg)

        #Adding Success Message in Logger
        loggin_debug.debug(success_msg)
