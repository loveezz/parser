class HeadersCreate:

    def __init__(self, cookie):
        self.__headers = None
        self.__cookie = cookie

    def get_headers(self):
        self.__headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0",
                          "Accept": "application/json, text/javascript, */*; q=0.01",
                          "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                          "Accept-Encoding": "gzip, deflate, br",
                          "X-Requested-With": "XMLHttpRequest",
                          "Connection": "keep-alive",
                          "Referer": "https://buff.163.com/market/csgo",
                          "Cookie": f"{str(self.__cookie).replace(' ', '')}",
                          "Sec-Fetch-Dest": "empty",
                          "Sec-Fetch-Mode": "cors",
                          "Sec-Fetch-Site": "same-origin",
                          "Pragma": "no-cache",
                          "Cache-Control": "no-cache"
                          }
        return self.__headers