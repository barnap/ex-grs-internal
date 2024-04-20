import dao.db_utils as db_utils
from dao import dao_conditions_info, dao_user
import config
import control
from utils import utils

def drop_database():
    drop_database_query = '''DROP DATABASE IF EXISTS  ''' + config.database + ''';'''
    db = db_utils.create_connection_dbms()
    cur = db.cursor()
    cur.execute(drop_database_query)

    print('Database deleted')
    db.close()

def check_databas_exists():
    exist_db_query = '''select exists(SELECT datname FROM pg_catalog.pg_database WHERE datname = %s );'''
    db = db_utils.create_connection_dbms()
    # cur = db.cursor()
    # cur.execute(drop_database_query)

    cur = db.cursor()
    cur.execute(exist_db_query, (config.database,))

    result = cur.fetchone()
    print('Executed the query')
    print(result[0])
    db.close()

    return result[0]


def create_database():
    # drop_database_query = '''DROP DATABASE IF EXISTS  ''' + config.database + ''';'''

    create_database_query = '''CREATE DATABASE ''' + config.database + '''
            WITH
            OWNER = %s
            TABLESPACE = pg_default
            CONNECTION LIMIT = -1
            IS_TEMPLATE = False;
        '''

    db = db_utils.create_connection_dbms()
    # cur = db.cursor()
    # cur.execute(drop_database_query)

    cur = db.cursor()
    cur.execute(create_database_query, (config.user,))

    print('Database created')
    db.close()


def create_user_table():
    create_user_table_query = '''CREATE TABLE IF NOT EXISTS public.user_app
        (
        PROLIFIC_ID text COLLATE pg_catalog."default" NOT NULL,
        Current_state text COLLATE pg_catalog."default",
        AGGREGATION text COLLATE pg_catalog."default",
        EXPLANATION text COLLATE pg_catalog."default",
        Start_time TIMESTAMPTZ,
        End_time TIMESTAMPTZ,
        Age_group text COLLATE pg_catalog."default",
        Gender text COLLATE pg_catalog."default",
        Name text COLLATE pg_catalog."default",
        Rest_1_0 text COLLATE pg_catalog."default",
        Rest_1_1 text COLLATE pg_catalog."default",
        Rest_1_2 text COLLATE pg_catalog."default",
        Rest_2_0 text COLLATE pg_catalog."default",
        Rest_2_1 text COLLATE pg_catalog."default",
        Rest_2_2 text COLLATE pg_catalog."default",
        Rest_3_0 text COLLATE pg_catalog."default",
        Rest_3_1 text COLLATE pg_catalog."default",
        Rest_3_2 text COLLATE pg_catalog."default",
        Rest_4_0 text COLLATE pg_catalog."default",
        Rest_4_1 text COLLATE pg_catalog."default",
        Rest_4_2 text COLLATE pg_catalog."default",
        Rest_5_0 text COLLATE pg_catalog."default",
        Rest_5_1 text COLLATE pg_catalog."default",
        Rest_5_2 text COLLATE pg_catalog."default",
        Friend_agree_1 text COLLATE pg_catalog."default",
        Friend_agree_2 text COLLATE pg_catalog."default",
        Friend_agree_3 text COLLATE pg_catalog."default",
        Friend_agree_4 text COLLATE pg_catalog."default",
        Friend_disagree_1 text COLLATE pg_catalog."default",
        Friend_disagree_2 text COLLATE pg_catalog."default",
        Friend_disagree_3 text COLLATE pg_catalog."default",
        Friend_disagree_4 text COLLATE pg_catalog."default",
        Uniform_start_timestamp TIMESTAMPTZ,
        Uniform_IND_fairness int,
        Uniform_IND_consensus int,
        Uniform_IND_satisfaction int,
        Uniform_GRP_fairness int,
        Uniform_GRP_consensus int,
        Uniform_GRP_satisfaction int,
        Uniform_feedback text COLLATE pg_catalog."default",
        Divergent_start_timestamp TIMESTAMPTZ,
        Divergent_IND_fairness int,
        Divergent_IND_consensus int,
        Divergent_IND_satisfaction int,
        Divergent_GRP_fairness int,
        Divergent_GRP_consensus int,
        Divergent_GRP_satisfaction int,
        Divergent_feedback text COLLATE pg_catalog."default",
        Coalitional_small_start_timestamp TIMESTAMPTZ,
        Coalitional_small_IND_fairness int,
        Coalitional_small_IND_consensus int,
        Coalitional_small_IND_satisfaction int,
        Coalitional_small_GRP_fairness int,
        Coalitional_small_GRP_consensus int,
        Coalitional_small_GRP_satisfaction int,
        Coalitional_small_feedback text COLLATE pg_catalog."default",
        Coalitional_large_start_timestamp TIMESTAMPTZ,
        Coalitional_large_IND_fairness int,
        Coalitional_large_IND_consensus int,
        Coalitional_large_IND_satisfaction int,
        Coalitional_large_GRP_fairness int,
        Coalitional_large_GRP_consensus int,
        Coalitional_large_GRP_satisfaction int,
        Coalitional_large_feedback text COLLATE pg_catalog."default",
        Minority_min_start_timestamp TIMESTAMPTZ,
        Minority_min_IND_fairness int,
        Minority_min_IND_consensus int,
        Minority_min_IND_satisfaction int,
        Minority_min_GRP_fairness int,
        Minority_min_GRP_consensus int,
        Minority_min_GRP_satisfaction int,
        Minority_min_feedback text COLLATE pg_catalog."default",
        Minority_maj_start_timestamp TIMESTAMPTZ,
        Minority_maj_IND_fairness int,
        Minority_maj_IND_consensus int,
        Minority_maj_IND_satisfaction int,
        Minority_maj_GRP_fairness int,
        Minority_maj_GRP_consensus int,
        Minority_maj_GRP_satisfaction int,
        Minority_maj_feedback text COLLATE pg_catalog."default",
        Underst_start_timestamp TIMESTAMPTZ,
        Underst_system_choice int,
        Underst_system_choice_feedback text COLLATE pg_catalog."default",
        Underst_best_choice int,
        Underst_best_feedback text COLLATE pg_catalog."default",
        Underst_end_timestamp TIMESTAMPTZ,
        General_feedback text COLLATE pg_catalog."default",
        Attention_uniform int,
        Attention_divergent int,
        Attention_coalitional_small int,
        Attention_coalitional_large int,
        Attention_minority_min int,
        Attention_minority_maj int,
        Attention_understandability int,
        CONSTRAINT user_pkey PRIMARY KEY (PROLIFIC_ID)
        )
        
        TABLESPACE pg_default;
        
        ALTER TABLE IF EXISTS public.user_app
        OWNER to ''' + config.user + ''';
    '''

    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute(create_user_table_query)

    db.commit()
    print('User table created')
    db.close()


# def create_playlist_table():
#     create_plylist_table_query = '''CREATE TABLE IF NOT EXISTS public.playlist_evaluation
#         (
#             song_id text COLLATE pg_catalog."default" NOT NULL,
#             user_id text COLLATE pg_catalog."default" NOT NULL,
#             relationship text COLLATE pg_catalog."default" NOT NULL,
#             self_eval double precision,
#             peer_eval double precision,
#             group_self_eval double precision,
#             is_original boolean,
#             peer_id text COLLATE pg_catalog."default",
#             CONSTRAINT playlist_evaluation_pkey PRIMARY KEY (song_id, user_id, relationship)
#         )
#
#         TABLESPACE pg_default;
#
#         ALTER TABLE IF EXISTS public.playlist_evaluation
#         OWNER to ''' + config.user + ''';
#     '''
#
#     db = db_utils.create_connection_db()
#     cur = db.cursor()
#     cur.execute(create_plylist_table_query)
#
#     db.commit()
#     print('Playlist table created')
#     db.close()


# def create_session_info_table():
#     create_session_info_table_query = '''CREATE TABLE IF NOT EXISTS public.session_info
#         (
#             id integer NOT NULL DEFAULT 1,
#             current_session integer NOT NULL DEFAULT 1,
#             CONSTRAINT session_info_pkey PRIMARY KEY (id)
#         )
#
#         TABLESPACE pg_default;
#
#         ALTER TABLE IF EXISTS public.session_info
#         OWNER to ''' + config.user + ''';
#     '''
#
#     db = db_utils.create_connection_db()
#     cur = db.cursor()
#     cur.execute(create_session_info_table_query)
#
#     db.commit()
#     print('Session info table created')
#     db.close()

def create_conditions_info_table():
    create_session_info_table_query = '''CREATE TABLE IF NOT EXISTS public.conditions_info
        (
            id integer NOT NULL DEFAULT 1,
            AGGREGATION text COLLATE pg_catalog."default",
            EXPLANATION text COLLATE pg_catalog."default",
            required int DEFAULT 37,
            assigned int DEFAULT 0,
            CONSTRAINT session_info_pkey PRIMARY KEY (id)
        )

        TABLESPACE pg_default;

        ALTER TABLE IF EXISTS public.conditions_info
        OWNER to ''' + config.user + ''';
    '''

    db = db_utils.create_connection_db()
    cur = db.cursor()
    cur.execute(create_session_info_table_query)

    db.commit()
    print('Conditions info table created')
    db.close()


if __name__ == '__main__':
    # print(dao_user.get_user_email_list())
    # user_email_list = dao_user.get_user_email_list()
    # for email in user_email_list:
    #     utils.send_email_start_session_2(email)

    # dao_session_info.init_session_info()

    if check_databas_exists():
        print("THE DATABASE ALREADY EXISTS")
    else:
        create_database()
        create_user_table()
        # create_playlist_table()
        create_conditions_info_table()
        dao_conditions_info.init_conditions_info()
        print("DATABASE CREATED")
        # print("CURRENT SESSION: ", dao_session_info.load_current_session())
