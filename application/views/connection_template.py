import os
from typing import Tuple
from collections import namedtuple

def cls():
    ''' Clear the console windows/Linux'''

    os.system('cls' if os.name=='nt' else 'clear')

def input_db_infos_page(db_type: str) -> Tuple[str]:
    ''' Get some informations for the dbExpor database for connection:
        :parram - db_type: The select type of DB (Server or Netchart)
        :return - Tuple with connections Informations 
    '''

    cls()

    # Creating a named tuple
    DB_infos = namedtuple('DatabaseInfo', 'host user passwd database')

    # Capture some informations From User
    print('Connection to {} !\n'.format(db_type))
    host = input('Insert the Server Host: ')
    user = input('Insert the User: ')
    passwd = input('Insert the Password: ')
    database = input('Insert the Database: ')

    # Confirm Decision
    confirm = input('\n\nConfirm the informations? (Y/N) : ')
    if confirm.startswith('Y') or confirm.startswith('y'):
        cls()
        return DB_infos(host=host,
                        user=user,
                        passwd=passwd,
                        database=database)
    else:
        # Close the program if not confirm
        print('\nClosing Program')
        input('Press Enter to exit...')
        exit(0)


