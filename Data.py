from os import getcwd

API_KEY = ""

links = [
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=120&extra_tag_ids=747&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=140&extra_tag_ids=865&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=100&extra_tag_ids=2180&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=80&extra_tag_ids=1086&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=190&extra_tag_ids=1216&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=700&extra_tag_ids=2887&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=125&extra_tag_ids=1335&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=180&extra_tag_ids=2574&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=225&extra_tag_ids=1476&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=119&extra_tag_ids=1523&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=420&extra_tag_ids=1596&sort_by=price.asc&wearless_sticker=1",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=300&extra_tag_ids=1802&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=230&extra_tag_ids=1831&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=750&extra_tag_ids=1878&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=175&extra_tag_ids=1927&sort_by=price.asc&wearless_sticker=",
    "https://buff.163.com/market/csgo#tab=selling&page_num=1&max_price=320&extra_tag_ids=1946&sort_by=price.asc&wearless_sticker=",
    ]


project_path = getcwd()

cookie_path = project_path + "/163Cookie.txt"
