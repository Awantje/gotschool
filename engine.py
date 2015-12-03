from __future__ import unicode_literals
from __future__ import print_function
import os
import sql
import got
import sys
import time
from io import StringIO
from colorama import init, deinit


DB_FILE_NAME = "got.db"
DB_FILE_NAME_QUOTED = '"' + DB_FILE_NAME + '"'
SCRIPT_FILE_NAME = "init_db.sql"
DB_TABLES = ["personages"]
SQL_TABLES_CHECK = "SELECT name FROM sqlite_master WHERE type='table'"


def check_db_file_exists():
    return os.path.isfile(DB_FILE_NAME)


def check_tables_exist():
    existing_tables_case_sensitive = sql.execute_sql(SQL_TABLES_CHECK)
    existing_tables = [table.lower() for table in existing_tables_case_sensitive]
    missing_tables = [should_exist for should_exist in DB_TABLES if should_exist not in existing_tables]
    if len(missing_tables) > 0:
        print("FOUT: De volgende tabellen missen in " + DB_FILE_NAME_QUOTED)
        for missing_table in missing_tables:
            print("  - " + missing_table)
        return False

    return True


def digits(number):
    return len(str(number))


def main():

    if not check_db_file_exists():
        sql.execute_script(SCRIPT_FILE_NAME)

    if not check_tables_exist():
        return -1

    game_state = {}

    sys.stdout = StringIO()
    got.init_game(game_state)

    ronde = 1

    while not got.is_game_over(game_state):

        sys.stdout = StringIO()
        print("------------------" + digits(ronde) * "-" + "------------")
        print("------      Ronde " + str(ronde) + "      ------")
        print("------------------" + digits(ronde) * "-" + "------------")

        game_state['Fase'] = 1
        got.toon_wereld_informatie(game_state)

        for fase in range(1, 2):
            if not got.is_game_over(game_state):
                got.speel_fase(game_state)
                actie = game_state['Actie']
                if actie != '':
                    method_name = actie
                    eval("got." + method_name + "(game_state)")

        if not got.is_game_over(game_state):
            got.verplaats(game_state)

        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__
        init()
        print(output)
        deinit()

        print("Verder in ", end='')
        sys.stdout.flush()
        for t in range(30, 0, -2):
            time.sleep(0.2)
            if t % 10 == 0:
                print(str(t // 10), end='')
            else:
                print(".", end='')

            sys.stdout.flush()

        print('')

        ronde += 1

    got.toon_game_over(game_state)

if __name__ == "__main__":
    main()
