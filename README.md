# Python_mySQL

## db.py

This is an importable module with codebase to connect to a mysql database. 
The DB class can be initialized by passing in the host name, database name and a path to your .cnf file which houses your db credentials.
Must always connect to the db using the conn() method.
You can pass your queries in the form of strings.

## dbupdate.py

Imports the db library and demonstrates it's use for a better understanding.
Notice the use of the below two lines to connect to the Database:
>self.mydb = DB(self.host, self.database)

>self.mydb.conn()
