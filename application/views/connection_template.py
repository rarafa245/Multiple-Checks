import os
from typing import Tuple
from collections import namedtuple

def cls():
    ''' Clear the console windows/Linux'''

    os.system('cls' if os.name=='nt' else 'clear')

def dbexport_db_info() -> Tuple[str]:
    ''' Get some informations for the dbExpor database for connection:
        :parram - None
        :return - Tuple with connections Informations 
    '''
    cls()

    # Creating a named tuple
    DB_infos = namedtuple('Database', 'host user passwd database')

    # Capture some informations From User
    print('Connection to Server DB Name (DBExport Database) !\n')
    host = input('Insert the Server Host: ')
    user = input('Insert the User: ')
    passwd = input('Insert the Password: ')
    database = input('Insert the Database: ')

    # Confirm Decision
    confirm = input('\n\nConfirm the informations? (Y/N) : ')
    if confirm.startswith('Y') or confirm.startswith('y'):
        return DB_infos(host=host,
                            user=user,
                            passwd=passwd,
                            database=database)
    else:
        # Close the program if not confirm
        print('\nClosing Program')
        input('Press Enter to exit...')
        exit(0)


