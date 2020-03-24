import mysql.connector
from typing import Tuple

class DB_Ids_Handler:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="172.16.128.6",
            user="movi_arg",
            passwd="QIz.1*B_1U.G7",
            database="netchart_mtn_nigeria_zte4g"
        )
        self.mycursor = self.mydb.cursor()
    
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