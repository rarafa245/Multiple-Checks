from application.models import *
from application.views import *

def main():

    start_page()
    
    # Connecting Databases
    host, user, passwd, db_DBexport, db_Netchart = input_db_infos_page()
    
    try:
        DBexport_db = DB_Server_Handler(host, user, passwd, db_DBexport)
        input('Press ENTER to continue...')
    except:
        print('Connection rejected, check the datas or contact the suport next time')
        input('Press ENTER...')
        exit(0)
    
    try:
        Netchart_db = DB_Netchart_Handler(host, user, passwd, db_Netchart)
        input('Press ENTER to continue...')
    except:
        print('Connection rejected, check the datas or contact the suport next time')
        input('Press ENTER...')
        exit(0)
    

    while True:
        command = options_page(DBexport_db.curDB, Netchart_db.curDB)

        if command == "1":
            print('Chose 1')
        elif command == "2":
            print('Chose 2')
        elif command == "3":
            print('Chose 3')
        elif command == "4":
            print('Chose 4')
        elif command == "9":
            exit(0)