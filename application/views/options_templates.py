import os

def cls():
    ''' Clear the console windows/Linux'''

    os.system('cls' if os.name=='nt' else 'clear')

def options_page(dbexport_db: str, netchart_db: str) -> str:
    ''' Creating a option menu '''

    cls()

    print('Databases:/n DBexport - {}\n Netchart - {}'.format(
        netchart_db, dbexport_db
    ))
    print('''
        Select a Command:

        1. Check data in DBexport Database
        2. Check data in Netchart Database
        3. Insert data in Netchart Database (One-By-One)
        4. Insert data in Netchart Database (File)
        9. Exit Program
    ''')
    choice = input('Command: ')
    return choice