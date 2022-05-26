class Database:
    def connect(self):
        pass

    def read(self, req: str) -> list:
        return []

    def write(self, req: str):
        pass

    # class Database has a join_table method which is not used for children
    def join_tables(self):
        pass


class MySQL(Database):
    def connect(self):
        pass

    def read(self, req: str) -> list:
        return []

    def write(self, req: str):
        pass

    def join_tables(self):
        pass


class MongoDB(Database):
    def connect(self):
        pass

    def read(self, req: str) -> list:
        return []

    def write(self, req: str):
        pass

    def join_tables(self):
        raise NotImplemented("mongo is relational db")
