import psycopg2

from data_works.db_configs.configure_db_parameters import config


def connect_to_db():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def inserting_new_value_groups(_ruz_id: int, _group_name: str, _description = ""):
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO groups(ruz_id, group_name, description) VALUES (%s,%s,%s)"""
        record_to_insert = (_ruz_id, _group_name, _description)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into GROUP table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into GROUP table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def inserting_new_value_users(_tg_id: int, _ruz_group_id: int, _first_name = "", _second_name = ""):
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO users(tg_id, ruz_group_id, first_name, second_name) VALUES (%s,%s,%s)"""
        record_to_insert = (_tg_id, _ruz_group_id, _first_name, _second_name)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into USERS table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into USERS table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
