class HttpClients:
    """basic class to make HTTP requests"""

    def get(self, url: str) -> dict:
        return {"message": f"get request for {url}"}

    def post(self, url: str, data: dict) -> dict:
        return {"message": f"post request for {url}"}

    def put(self, url: str, data: dict) -> dict:
        return {"message": f"put request for {url}"}


class UserFetcher(HttpClients):
    """class to operate user data"""

    def get_one_user(self, uid: int) -> dict:
        return self.get(f"http://localhost:8000/{uid}")

    def get_all_users(self):
        return self.get(f"http://localhost:8000/")


class DataFetcher(HttpClients):
    """class to operate requests"""

    def create_request(self, data) -> dict:
        return self.post("http://localhost:8000/request/", data)

    def get_request(self, uid: int) -> dict:
        return self.get(f"http://localhost:8000/request/{uid}")

    def put_request(self, uid: int, data: dict) -> dict:
        return self.put(f"http://localhost:8000/request/{uid}", data)
