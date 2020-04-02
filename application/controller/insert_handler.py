from application.models import *
from application.views import *
from .options_handler import *

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
            # Check Table in DBexport DB
            check_table_DBexport(DBexport_db)

        elif command == "2":
            # Check Table in Netchart DB
            check_table_Netchart(Netchart_db)

        elif command == "3":
            # Insert one table in Netchart DB _table_IDs
            insert_one_register(DBexport_db, Netchart_db)

        elif command == "4":
            # Insert one table in Netchart DB _table_IDs
            insert_file_register(DBexport_db, Netchart_db)
            
        elif command == "9":
            exit(0)