from typing import List

def check_table_DBexport(DBexport_db: object, table_name=None) -> List[str]:
    ''' Checking if the input table is is DBexport DB
        :parram - Object with DBexport Connection
        :return - pks : List with pks from DBexport DB
                - None
    '''

    if not table_name:
        table = input('\n\nInsert a table name: ')
    else:
        table = table_name
    

    if DBexport_db.check_data(table):
        # if table in DBexport DB, print it

        print('\ntable a_{} present in {}'.format(
            table, DBexport_db.curDB
        ))

        # Printing PKs
        print('Primary Keys: ')
        pks = DBexport_db.get_pks(table)
        for i, element in enumerate(pks):
            print('{} --> {}'.format(i, element))
        input('\nPress ENTER to Continue...')

        # returning pks
        return pks
    else:
        # if table not in Dbexport DB, print it

        print('table a_{} NOT present in {}'.format(
            table, DBexport_db.curDB
        ))
        input('\nPress ENTER to Continue...')

        # Returning none
        return None


def check_table_Netchart(Netchart_db: object, table_name=None) -> bool:
    ''' Checking if the input table is is DBexport DB
        :parram - Object with Netchart Connection
        :return - None
    '''

    if not table_name:
        table = input('\n\nInsert a table name: ')
    else:
        table = table_name

    if Netchart_db.check_data(table):
        # if table in Netchart DB, print it 

        print('\ntable {} present in {}._table_ids'.format(
            table, Netchart_db.curDB
        ))
        input('\nPress ENTER to Continue...')
        return True
    else:
        # if table not in Dbexport DB, print it

        print('table {} NOT present in {}._table_ids'.format(
            table, Netchart_db.curDB
        ))
        input('\nPress ENTER to Continue...')
        return False