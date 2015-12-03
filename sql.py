from __future__ import unicode_literals
from __future__ import print_function
import sqlite3

DB_FILE_NAME = "got.db"
DB_FILE_NAME_QUOTED = '"' + DB_FILE_NAME + '"'


def execute_script(filename):

    with open(filename, "r") as scriptfile:
        con = sqlite3.connect(DB_FILE_NAME)
        try:
            script = scriptfile.read()
            con.executescript(script)
        except Exception as e:
            print("FOUT: " + e.message)
        finally:
            con.close()


def execute_sql(query, *args):

    results = []

    if sqlite3.complete_statement(query + ";"):
        con = sqlite3.connect(DB_FILE_NAME)
        try:
            cur = con.execute(query + ";", args)
            result_rows = cur.fetchall()
            results = [tup[0] for tup in result_rows]
        except Exception as e:
            print("FOUT in '" + query + "' : " + e.message)
        finally:
            con.close()
    else:
        print("GEEN GELDIGE QUERY: " + query)

    return results


def column(query, *args):
    results = execute_sql(query, *args)
    return results
