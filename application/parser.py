from application.logging_manager import create_logging_debug
from application.models import *

loggin_debug = create_logging_debug(__name__)

def main():

    Ids_Table = DB_Ids_Handler()
    Technology = DB_Tech_Handler()

    with open('rec/parser.txt', 'r') as f:
        lines = f.readlines()
        for table in lines:
            #Pegar Linha
            raw_table = table.split('\n')
            loggin_debug.debug(raw_table[0])
            
            if Ids_Table.check_data(raw_table[0]):
                print(raw_table[0] + 'In table _tables_id !')

            #Triar PKs
            pk = Technology.get_pks(raw_table[0])
            if 'DATEDAY' in pk: pk.remove('DATEDAY')
            elif 'dateday' in pk: pk.remove('dateday')

            tableIDs = ",".join(pk)
            loggin_debug.debug('PKs: ' + tableIDs)

            resp = Ids_Table.add_data(raw_table[0], tableIDs)
            loggin_debug.debug(resp)
            

