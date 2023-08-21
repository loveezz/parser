import random

import httpx
import asyncio

from Backend.CookieHandler import CookieHandler
from Backend.HeadersCreate import HeadersCreate
from Backend.UrlConverter import UrlConverter

from Data import cookie_path, links

from json import loads


class Parser:
    def __init__(self):
        self.__requests = None

        self.__status = True

        self.__client = httpx.AsyncClient()

        self.__cookie = CookieHandler(cookie_path)
        self.__headers = HeadersCreate(self.__cookie.get_cookie()).get_headers()

        self.__converter = UrlConverter(links)

        self.links_list = self.__converter.get_links_list()

        self.__update_dict = dict()

        self.__notification_status = False

        self.__item_urls = list()

    async def change_links(self, links_list):
        self.__converter = UrlConverter(links_list)

        self.links_list = self.__converter.get_links_list()

        if not self.links_list:
            self.__converter = UrlConverter(links)

            self.links_list = self.__converter.get_links_list()
            return False
        return True
    def __request_to_link(self, link):
        async def request():
            self.__requests = await self.__client.get(link, headers=self.__headers)

            self.__get_changes(self.__requests.text, link)

        return asyncio.create_task(request())

    async def start(self, link):
        if not self.__status:
            return

        await self.__request_to_link(link)

        time_sleep = random.randrange(5, 15)
        await asyncio.sleep(time_sleep)

        return

    async def check_notification(self):
        if self.__notification_status:
            self.__notification_status = False
            return_list = self.__item_urls
            self.__item_urls = list()
            return return_list
        return

    async def get_status(self):
        return self.__status

    async def set_status(self, status: bool):
        self.__status = status

    def __get_changes(self, response, link):
        id_list = list()

        if link in self.__update_dict.keys():
            id_list_old = self.__update_dict[link]

            items = loads(response)['data']['items']
            for item in items:
                id_list.append(int(item['id']))
            if len(id_list_old) == 0:
                changes = list(id_list)
                for id_change in changes:
                    for item in items:
                        if int(item['id']) == id_change:
                            item_url = self.__converter.get_item_url(link, item['id'])
                            self.__notification_status = True
                            self.__item_urls.append([item_url, item["goods_info"]["original_icon_url"], item["market_hash_name"], item["sell_min_price"]])
                            return
            if len(id_list_old) == len(id_list) and len(id_list_old) != 0:
                if id_list_old[0] != id_list[0]:
                    self.__update_dict[link] = id_list
                    try:
                        changes = list(id_list[:id_list.index(id_list_old[0])])
                    except:
                        changes = id_list
                    for id_change in changes:
                        for item in items:
                            if int(item['id']) == id_change:
                                item_url = self.__converter.get_item_url(link, item['id'])
                                self.__notification_status = True
                                self.__item_urls.append([item_url, item["goods_info"]["original_icon_url"], item["market_hash_name"], item["sell_min_price"]])
                                return

        else:
            items = loads(response)['data']['items']
            for item in items:
                id_list.append(int(item['id']))
            # id_list.sort()
            self.__update_dict[link] = id_list
            return
