import os

def cls():
    ''' Clear the console windows/Linux'''

    os.system('cls' if os.name=='nt' else 'clear')

def start_page():
    ''' Elements For the Start Page. Basic Informations
        :parram - None
        :return - None
    '''
    print('Netchart - Multiple Checks Program Tables Handler\n')
    print('\t Version: 2.1.1 \t\t (Rafael Ferreira)\n\n')
    print(''' 
                This Program was created with the purpose of maintaining elements 
            in tables for the Multiple Checks function.
                For Any problems, contact the suport
    ''')
    input('Press ENTER to continue...')