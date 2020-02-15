# database.py
#
# This module simplifies interaction with a database.
#
# Install the mariaDB database server:
#     sudo apt-get install mariadb-server
#
# Install the connector for mariaDB:
#     $pip3 install mysql-connector-python
#
# Useful links:
#     https://mariadb.com/kb/en/documentation/
#     https://dev.mysql.com/doc/connector-python/en/


import mysql.connector as db


dbConfig = {"pool_name": "botpool",
            "pool_reset_session": False,  # set to true when pooling is fixed
            "pool_size": 1,  # set to 10 when pooling is fixed
            "host": "localhost",
            "user": "lathrem",
            "passwd": "poros",
            "database": "lathremBot"}


def create(sql, data={}):
    """
    This function is used to create a new record in the database. It returns
    a tuple containint the number of rows affected and the value generated for
    an AUTO_INCREMENT column or None when there is no such value available.

    Keyword arguments:
    sql -- A string containing the INSERT statement to execute.
    data -- An optional tuple or dict containing the values to bind.
    """
    cnx = db.connect(**dbConfig)  # get a connection from the pool
    cur = cnx.cursor()  # create a cursor to hold the results of our sql
    result = (0, 0)
    try:
        cur.execute(sql, data)  # run the sql
        result = (cur.rowcount, cur.lastrowid)  # get the data to return
        cnx.commit()  # save the changes
    except db.Error as e:
        print(f"Database error: {e}")
    finally:
        cur.close()  # close the cursor
        cnx.close()  # close the connection
    return result


def read(sql, data={}):
    """
    This function is used to read data in the database. This returns all of
    the selected data in a list of tuples.

    Keyword arguments:
    sql -- A string containing the SELECT statement to execute.
    data -- An optional tuple or dict containing the values to bind.
    """
    cnx = db.connect(**dbConfig)  # get a connection from the pool
    cur = cnx.cursor()  # create a cursor to hold the results of our sql
    result = ()
    try:
        cur.execute(sql, data)  # run the sql
        result = cur.fetchall()  # get the data to return
    except db.Error as e:
        print(f"Database error: {e}")
    finally:
        cur.close()  # close the cursor
        cnx.close()  # close the connection
    return result


def update(sql, data={}):
    """
    This function is used to update records in the database. It returns
    the number of rows affected.

    Keyword arguments:
    sql -- A string containing the UPDATE statement to execute.
    data -- An optional tuple or dict containing the values to bind.
    """
    cnx = db.connect(**dbConfig)  # get a connection from the pool
    cur = cnx.cursor()  # create a cursor to hold the results of our sql
    result = 0
    try:
        cur.execute(sql, data)  # run the sql
        result = cur.rowcount  # get the return value
        cnx.commit()  # saves the changes
    except db.Error as e:
        print(f"Database error: {e}")
    finally:
        cur.close()  # close the cursor
        cnx.close()  # close the connection
    return result


def delete(sql, data={}):
    """
    This function is used to delete records in the database. It returns
    the number of rows affected.

    Keyword arguments:
    sql -- A string containing the DELETE statement to execute.
    data -- An optional tuple or dict containing the values to bind.
    """
    cnx = db.connect(**dbConfig)  # get a connection from the pool
    cur = cnx.cursor()  # create a cursor to hold the results of our sql
    result = 0
    try:
        cur.execute(sql, data)  # run the sql
        result = cur.rowcount  # get the return value
        cnx.commit()  # saves the changes
    except db.Error as e:
        print(f"Database error: {e}")
    finally:
        cur.close()  # close the cursor
        cnx.close()  # close the connection
    return result
