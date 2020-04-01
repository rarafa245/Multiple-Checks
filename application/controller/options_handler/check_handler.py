def check_table_DBexport(DBexport_db):

    table = input('\n\nInsert a table name: ')

    if DBexport_db.check_data(table):
        print('table a_{} present in {}'.format(
            table, DBexport_db.curDB
        ))
        print('Primary Keys: ')
        for i, pks in enumerate(DBexport_db.get_pks(table)):
            print('{} --> {}'.format(i, pks))
    else:
        print('table a_{} NOT present in {}'.format(
            table, DBexport_db.curDB
        ))
    input('\nPress ENTER to Continue...')


def check_table_Netchart(Netchart_db):

    table = input('\n\nInsert a table name: ')

    if Netchart_db.check_data(table):
        print('table {} present in {} _table_ids'.format(
            table, Netchart_db.curDB
        ))
    else:
        print('table {} NOT present in {}'.format(
            table, Netchart_db.curDB
        ))
    input('\nPress ENTER to Continue...')