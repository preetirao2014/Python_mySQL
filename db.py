from __future__ import print_function
import MySQLdb as mdb
from MySQLdb.constants import FIELD_TYPE
import sys
import logging
import traceback
import re


class DB:
    def __init__(self, h, d, c='~/.my.cnf'):
        self.host = h
        self.db = d
        self.conf = c
        self.con = None
        self.conversion = {
            FIELD_TYPE.TINY: int,
            FIELD_TYPE.SHORT: int,
            FIELD_TYPE.INT24: int,
            FIELD_TYPE.LONG: int,
            FIELD_TYPE.LONGLONG: long,
            FIELD_TYPE.FLOAT: float,
        }

    def conn(self):
        '''
        Connects to a supplied host and return a MySQLdb connection object.
        Connection is persisted in the self.con attribute

        :return: MySQL connection or false
        '''
        try:
            connection = mdb.connect(
                host=self.host,
                db=self.db,
                read_default_file=self.conf,
                conv=self.conversion
            )
            logging.info(
                'db: connected to database %s at %s'
                % (self.db, self.host)
            )
            self.con = connection
            return self.con
        except Exception as e:
            logging.error(
                'db: failed to connect to database Exception: '
                '%s System info : %s'
                % (e, sys.exc_info()[1])
            )
            return False

    def _query(self, query):

        logging.info('executing query: %s' % query)
        try:
            cursor = self.con.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            logging.info(
                'db: query successful, returned %s rows' % str(len(result))
            )
            return result
        except mdb.ProgrammingError:
            logger.error('db: invalid query')
            raise mdb.ProgrammingError

    def query(self, q, p):
        return self._query(q % p)

    def query_without_args(self, q):

        return self._query(q)

    def insert_for_key(self, q, p):

        self._query(q % p)
        self.con.commit()
        return True

    def commit(self):
        self.con.commit()
        return True

    def insert_for_key_no_args(self, q):

        self._query(q)
        self.con.commit()
        return True

    def subquery(self, q, p):
        try:
            cur = self.con.cursor()
            cur.execute(q, p)
            result = cur.fetchall()
            logging.info(
                'db: query successful, returned %s rows' % str(len(result))
            )
            return result
        except Exception as e:
            logging.error(
                'db: failed to query Exception: %s' % traceback.format_exc()
            )

    def close(self):
        try:
            self.con.close()
            logging.info('db: connection to database closed')
        except:
            logging.error(
                'db: failed to close connection with error : %s'
                % sys.exc_info()[1]
            )

    def conExeClo(self, q, p):
        con = self.conn()
        result = self.query(q, p)
        self.close()
        return result
