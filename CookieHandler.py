from json import loads


class CookieHandler:

    def __init__(self, cookie_path):
        self.__cookie_path = cookie_path
        self.__cookie = None

    @staticmethod
    def read_cookie(path):
        try:
            with open(path, 'r') as f:
                cookie = loads(f.read())
                f.close()
        except Exception as ex:
            raise Exception(f"Неправильный формат файла куки!\n{ex}")

        if cookie:
            return cookie
        return

    def get_cookie(self):

        if self.__cookie is None:
            self.__cookie = self.read_cookie(self.__cookie_path)

            cookies = str()
            for cook in self.__cookie:
                cookies += f"{cook['name']}={cook['value']}; "

            self.__cookie = cookies
        return self.__cookie




