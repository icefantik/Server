from mysql.connector import connect, Error

class Database:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.pwd = "mpa0304029zawery"

        self.name_db = "wdef"
        self.table_usr = "users"
        self.connection = None

    def connect(self):
        try:
            with connect(
                host=self.host,
                user=self.user,
                password=self.pwd,
            ) as connection:
                self.connection = connection
                query_use_db = "use %s" % self.name_db
                query = "SELECT * FROM %s" % self.table_usr
                with connection.cursor() as cursor:
                    cursor.execute(query_use_db)
                    cursor.execute(query)
                    for db in cursor:
                        print(db)
                    connection.commit()
        except Error as e:
            print(e)

    def run_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def create_db(self):
        pass