import random

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


def inserting_new_value_users(_tg_id: int, _ruz_group_id: int, _username=""):
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO users(tg_id, group_id, username) VALUES (%s,%s,%s)"""
        record_to_insert = (_tg_id, _ruz_group_id, _username)
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


def inserting_new_value_schedule(_discipline: str, _date: str, _auditorium="No info about this", _dayOfWeekString="No info about this",
                                 _beginLesson="No info about this", _endLesson="No info about this", _kindOfWork="No info about this",
                                 _lecturer="No info about this", _lecturer_email="No info about this", _zoom_url="No info about this"):
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        new_id = random.randint(10000, 99999)
        while 1:

            postgres_check_id_query = f"""SELECT exists(SELECT 1 FROM schedule WHERE id={new_id})I"""
            cursor.execute(postgres_check_id_query)
            if not bool(cursor.fetchone()[0]):
                break
            new_id = random.randint(10000, 99999)

        postgres_insert_query = """INSERT INTO schedule(id, auditorium, discipline, date, "beginLesson", "endLesson", 
        "kindOfWork", lecturer, lecturer_email, zoom_url, "dayOfWeekString") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s) """
        record_to_insert = (new_id, _auditorium, _discipline, _date, _beginLesson, _endLesson, _kindOfWork,
                            _lecturer, _lecturer_email, _zoom_url, _dayOfWeekString)

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

