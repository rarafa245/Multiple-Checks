from .check_handler import check_table_DBexport, check_table_Netchart

def insert_one_register(DBexport_db: object, Netchart_db: object, table_name=None)  -> bool:
    ''' Add one register in Netchart DB._table_ids 
        :parram - Objects with Databases Connections
        :return - Bool with success or not success (True/False)
    '''

    if not table_name:
        table = input('\n\nInsert a table name: ')
    else:
        table = table_name

    pks = check_table_DBexport(DBexport_db, table)
    if not pks:
        # Return if table not in DBexport DB
        
        return False
    else:
        # If table in DBexport DB, and catched the PKs, check in Netchart DB

        if not check_table_Netchart(Netchart_db, table):
            #  If table alsow in Netchart DB._tables_ids, insert the data

            confirm = input('Are you sure to insert table "{}" in {}._table_ids? (Y/N): '.format(
                table, Netchart_db.curDB
            ))

            if confirm.startswith('Y') or confirm.startswith('y'):

                tableIDs = ",".join(pks)
                
                Netchart_db.add_data(table, tableIDs)
                input('\nPress ENTER to Continue...')
                return True
            else:

                input('Returning... \nPress ENTER to Continue...')
                return False
        else:
            return False


def insert_file_register(DBexport_db: object, Netchart_db: object)  -> bool:
    ''' Add one register in Netchart DB._table_ids comming from file 
        :parram - Objects with Databases Connections
        :return - Bool with success or not success (True/False)
    '''

    # Collecting and Printing Tables in selected File
    print('\n\n\tTables in File: \n')
    with open('rec/exporter.txt', 'r') as f:
        lines = f.readlines()
        for i, table in enumerate(lines):
            raw_table = table.split('\n')
            print('{}. -- {}'.format(i, raw_table[0]))
    
    confirm = input('\nAre you sure you want to insert all tables ? (Y/N) : ')

    # Adding Tables using insert_one_register function
    if confirm.startswith('Y') or confirm.startswith('y'):
        with open('rec/exporter.txt', 'r') as f:
            lines = f.readlines()
            for table in lines:
                raw_table = table.split('\n')
                if not insert_one_register(DBexport_db, Netchart_db, raw_table[0]):
                    break
            else:
                print('All Tables were registered!')
                input('\nPress ENTER to Continue...')
                return True
            
            print('\n\nStopped in table {}. Stopped Process!'.format(table))
            input('\nPress ENTER to Continue...')
            return False
    else:
        input('Returning... \nPress ENTER to Continue...')
        return False
