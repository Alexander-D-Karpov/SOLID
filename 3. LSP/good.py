class Database:
    def __init__(self, name):
        self.name = name

    def connect(self):
        print(f"Connected to {self.name}")
        pass

    def read(self, req: str) -> list:
        return []

    def write(self, req: str):
        pass


class SQLDB(Database):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def join_tables(self):
        pass


class NoSQLDB(Database):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def create_index(self):
        pass


class MySQL(SQLDB):
    def __init__(self):
        name = "MySQL"
        super().__init__(name)
        self.name = name

    def get_db(self):
        return self.name


class PostgresQL(SQLDB):
    def __init__(self):
        name = "PostgresQL"
        super().__init__(name)
        self.name = name

    def get_db(self):
        return self.name


class MongoDB(NoSQLDB):
    def __init__(self):
        name = "MongoDB"
        super().__init__(name)
        self.name = name

    def get_db(self):
        return self.name


# so we can use something like that:


def connect_to_db(database: Database):
    database.connect()


postgres = PostgresQL()
mysql = MySQL()
mongo = MongoDB()

connect_to_db(postgres)
connect_to_db(mysql)
connect_to_db(mongo)
