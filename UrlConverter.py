import re
from time import time

import logging

class UrlConverter:
    def __init__(self, links):
        self.__links = links
        self.__req_links = list()

    @staticmethod
    def __convert_ulr(link, category, item_id=""):
        try:
            params = re.search(r'&\S+', link)
            params = params[0]

            if category == "req":
                game = re.search(r'/\w+#', link)[0][1:][:-1]
        except:
            logging.error(f"Неправильная ссылка для фильтров! {link}")
            return
        time_ = str(time()).replace(".", "")[:-3]
        if category == "req":
            req_url = f"https://buff.163.com/api/market/goods?game={game}{params}&use_suggestion=0&_={time_}"
            return req_url
        elif category == "item":
            if item_id:
                item_url = f"https://buff.163.com/goods/{item_id}?from=market#tab=selling{params}"
                return item_url

    def get_links_list(self):
        for link in self.__links:
            link = self.__convert_ulr(link, "req")
            if link:
                self.__req_links.append(link)

        return self.__req_links

    def get_item_url(self, link, item_id):
        return self.__convert_ulr(link, "item", item_id)



