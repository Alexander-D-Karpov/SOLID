class DataFetcher:
    """a lot of functions -> bad"""

    def get(self, url):
        pass

    def post(self, url, data):
        pass

    def put(self, url, data):
        pass

    def delete(self, url):
        pass

    def get_user(self, id):
        return self.get(f"localhost:8000/{id}")

    def get_request(self, id):
        return self.get(f"localhost:8000/request/{id}")

    def get_clients(self):
        return self.get(f"localhost:8000/clients")
