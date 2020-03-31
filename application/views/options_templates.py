import os

def cls():
    ''' Clear the console windows/Linux'''

    os.system('cls' if os.name=='nt' else 'clear')

def options_page():
    ''' Creating a option menu '''

    print('''
        1. Check data in DBexport Database
        2. Check data in Netchart Database
        3. Insert data in Netchart Database (One-By-One)
        4. Insert data in Netchart Database (File)
        9. Exit Program
    ''')
    choice = input('Command: ')
    return choice