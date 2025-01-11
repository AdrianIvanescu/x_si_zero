from colorama.ansi import Fore
from colorama.ansi import Style

from .db_connection import DbConnection


class CreateTable():
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_conn = DbConnection(db_name)

    def create_table(self):
        # create table as per requirement
        sql = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name}(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        A CHAR(10) NOT NULL,
        B CHAR(10) NOT NULL,
        C CHAR(10) NOT NULL
        );
        """

        sql1 = f"""
         INSERT INTO {self.table_name} (A,B,C)
        VALUES('-','-','-');
        """

        self.db_conn.open_db_connection()
        self.db_conn.execute_sql(sql)
        self.db_conn.execute_sql(sql1)
        self.db_conn.execute_sql(sql1)
        self.db_conn.execute_sql(sql1)
        self.db_conn.commit_db_change()
        self.db_conn.close_db_connection
        print(
            f'''>> The table {Fore.GREEN}{self.table_name}{Style.RESET_ALL} \
created successfully...'''
        )
