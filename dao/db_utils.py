import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config
sys.path.append('../')


def create_connection_db():
    '''
    Creates connection to the database!
    :return:
    '''
    connection = psycopg2.connect(user=config.user,
                                  password=config.password,
                                  host=config.host,
                                  port=config.port,
                                  database=config.database)
    return connection


def create_connection_dbms():
    '''
    Creates connection to the database!
    :return:
    '''
    # con = psycopg2.connect("user=test password='test'");
    connection = psycopg2.connect(user=config.user,
                                  password=config.password,
                                  host=config.host,
                                  port=config.port)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

    return connection


