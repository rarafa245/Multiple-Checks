import mysql.connector
from typing import Tuple

class DB_Tech_Handler:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="172.16.128.6",
            user="movi_arg",
            passwd="QIz.1*B_1U.G7",
            database="zte_oss_param_4g_mtn_nigeria_csv"
        )
        self.mycursor = self.mydb.cursor()
    
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
    
    
