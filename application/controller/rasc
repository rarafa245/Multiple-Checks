import os
from application.logging_manager import create_logging_debug
from application.models import *

loggin_debug = create_logging_debug(__name__)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():

    cls()
    print('Starting Program...')

    Ids_Table = DB_Ids_Handler()
    Technology = DB_Tech_Handler()

    while True:
        
        cls()
        input_table = input('Insert a Table: ')
        loggin_debug.debug('Insert a Table {}'.format(input_table))

        if Ids_Table.check_data(input_table):
            print('Table registrated in _tables_id!')
            loggin_debug.debug('Table registrated in _tables_id!')
            input('press enter to continue...')
            
            return False
        else:
            print('Table not registrated in _tables_id!')
            loggin_debug.debug('Table not registrated in _tables_id!')
            input('press enter to continue...')

        apply = input('Insert the Table in {} ? Y/N : '.format(input_table))
        loggin_debug.debug('Insert in DB: {}'.format(apply))
        if apply.startswith('Y') or apply.startswith('y'):
            
            pk = Technology.get_pks(input_table)
            if 'DATEDAY' in pk: pk.remove('DATEDAY')
            elif 'dateday' in pk: pk.remove('dateday')

            tableIDs = ",".join(pk)
            print('PKs: {}'.format(tableIDs))
            loggin_debug.debug('PKs: ' + tableIDs)

            sure = input('Are you sure to insert the datas? Y/N: ')
            loggin_debug.debug('Are you sure to insert the datas? Y/N: {}'.format(sure))
            if sure.startswith('N') or sure.startswith('n'): return
            elif sure.startswith('Y') or sure.startswith('y'):
                resp = Ids_Table.add_data(input_table, tableIDs)
                loggin_debug.debug(resp)
                print(resp)
                input('press enter to continue...')
            else:
                print('Invalid command!')

        elif apply.startswith('N') or apply.startswith('n'):
            print('Bye!')
            return
        else:
            print('Invalid Command, Exiting!')
            return
