#!/usr/bin/env python2.7
"""Connector to DB"""
from operator import itemgetter
from datetime import datetime
from db import DB

class ConnectETE:

    """Class to interact with tables studentslist and campuslist"""

    def __init__(self):
        self.host = 'some.dummy.hostname.net'
		self.database = 'University'
        self.mydb = DB(self.host, self.database)
        self.mydb.conn()

    def get_data(self, sid, cid):

        """returns concatenation of student name and campus name"""

        sid = self.data['sid']
        cid = self.data['cid']
        query = None
        query = ('''select concat(b.namefield,' - ', a.namefield)
                    from studentslist a, campuslist b
                    where sid = %s
                    and cid = %s ''')
        if query is None:
            return None
        result = self.mydb.query(query, (sid, cid))
        if result:
            return result
        else:
            return False

    def create_student_entry(self, name, id):

        """creates a student entry in studentslist table"""

        now = datetime.now()
        query = None
        query = ('''insert into studentslist
                    (sid, namefield, created, lastupdated)
                    values (\'{}\', \'{}\', \'{}\', \'{}\') '''.format(
                        id, name, now, now))
        if query is None:
            return None
        result = self.mydb.insert_for_key_no_args(query)
        return result
