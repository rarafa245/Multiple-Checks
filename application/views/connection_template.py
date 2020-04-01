import os
from typing import Tuple
from collections import namedtuple

def cls():
    ''' Clear the console windows/Linux'''

    os.system('cls' if os.name=='nt' else 'clear')

def input_db_infos_page() -> Tuple[str]:
    ''' Get some informations for the dbExpor database for connection:
        :parram - None
        :return - Tuple with connections Informations 
    '''

    cls()

    # Creating a named tuple
    DB_infos = namedtuple('DatabaseInfo', 'host user passwd db_DBexport db_Netchart')

    # Capture some informations From User
    print('Connection to Server: !\n')
    host = input('Insert the Server Host: ')
    user = input('Insert the User: ')
    passwd = input('Insert the Password: ')
    print('\n\nInsert Databases:')
    database0 = input('\nInsert Server Database (DBexport): ')
    database1 = input('Insert Netchart Database: ')

    # Confirm Decision
    confirm = input('\n\nConfirm the informations? (Y/N) : ')
    if confirm.startswith('Y') or confirm.startswith('y'):
        cls()
        return DB_infos(host=host,
                        user=user,
                        passwd=passwd,
                        db_DBexport=database0,
                        db_Netchart=database1)
    else:
        # Close the program if not confirm
        print('\nClosing Program')
        input('Press Enter to exit...')
        exit(0)


