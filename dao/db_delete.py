import dao.db_utils as db_utils
import config


def drop_database():
    drop_database_query = '''DROP DATABASE IF EXISTS  ''' + config.database + ''';'''
    db = db_utils.create_connection_dbms()
    cur = db.cursor()
    cur.execute(drop_database_query)

    print('Database deleted')
    db.close()


if __name__ == '__main__':
    drop_database()

