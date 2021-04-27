import time
import psycopg2
import logging
from app.credentials import postgresql_credentials as cred
from app.core import query_builder as query

logging.basicConfig(level=logging.INFO)


class FortuneCookieModel(object):

    @classmethod
    def init_data(cls, data):
        con = psycopg2.connect(database=cred.database,
                               user=cred.user,
                               password=cred.password,
                               host=cred.host,
                               port=cred.port)
        cur = con.cursor()
        start_time = time.time()
        try:
            cur.execute(query.create_table_query())
            cur.executemany(query.insert_rows_query(), data)
            con.commit()
        except Exception as e:
            logging.info(e)
        finally:
            cur.close()
            con.close()
            logging.info(('Elapsed time in saving: %s' % (time.time() - start_time)))

    @classmethod
    def get_fortune(cls):
        response = None
        con = psycopg2.connect(database=cred.database,
                               user=cred.user,
                               password=cred.password,
                               host=cred.host,
                               port=cred.port)
        cur = con.cursor()
        start_time = time.time()
        try:
            cur.execute(query.get_fortune_query())
            response = cur.fetchone()
        except Exception as e:
            logging.info(e)
        finally:
            cur.close()
            con.close()
        logging.info(('Elapsed time in retrieving: %s' % (time.time() - start_time)))
        return response

    @classmethod
    def save_fortune(cls, data):
        con = psycopg2.connect(database=cred.database,
                               user=cred.user,
                               password=cred.password,
                               host=cred.host,
                               port=cred.port)
        cur = con.cursor()
        start_time = time.time()
        try:
            cur.execute(query.save_fortune_query(), (data['fortune'], int(data['id'])))
            con.commit()
        except Exception as e:
            logging.info(e)
        finally:
            cur.close()
            con.close()
            logging.info(('Elapsed time in saving: %s' % (time.time() - start_time)))