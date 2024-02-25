import config
import pymssql


class DatabaseExecutor:

    @staticmethod
    def execute_query(sql_query):
        try:
            with pymssql.connect(
                host=config.db_server,
                user=config.db_user,
                password=config.db_password,
                database=config.db_name,
                as_dict=True,
            ) as connection:
                with connection.cursor() as cursor:
                    print("Connection with database is done.")
                    cursor.execute(sql_query)
                    print("The query was executed: ", sql_query)

        except Exception as e:
            print("Error executing the query:", str(e))
            raise