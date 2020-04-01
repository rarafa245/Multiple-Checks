import mysql.connector

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

        self.mycursor.execute("SELECT tableName FROM _table_ids")
        myresult = self.mycursor.fetchall()

        for element in myresult:
            if data.lower() in element or data.upper() in element:
                return True
        else:
            return False

    def add_data(self, tableName, tableIDs):

        sql = "INSERT INTO _table_ids (tableName, tableIDs) VALUES (%s, %s)"
        val = (tableName, tableIDs)

        self.mycursor.execute(sql, val)
        self.mydb.commit()

        return (self.mycursor.rowcount, "record inserted.")
