from application.models import DB_Server_Handler
from application.views import *

def main():

    start_page()
    
    # Connecting Databases
    DBexport_db_infos = input_db_infos_page('Server DB Name (DBexport Database)')
    try:
        DBexport_db = DB_Server_Handler(DBexport_db_infos.host, DBexport_db_infos.user,
                                    DBexport_db_infos.passwd, DBexport_db_infos.database)
        input('Press ENTER to continue...')
    except:
        print('Connection rejected, check the datas or contact the suport next time')
        input('Press ENTER...')
        exit(0)
    
    Netchart_db_infos = input_db_infos_page('Netchart DB Name')
    try:
        Netchart_db = DB_Server_Handler(Netchart_db_infos.host, Netchart_db_infos.user,
                                    Netchart_db_infos.passwd, Netchart_db_infos.database)
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