from .check_handler import check_table_DBexport, check_table_Netchart

def insert_one_register(DBexport_db: object, Netchart_db: object)  -> bool:
    ''' Add one register in Netchart DB._table_ids 
        :parram - Objects with Databases Connections
        :return - Bool with success or not success (True/False)
    '''

    table = input('\n\nInsert a table name: ')

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
