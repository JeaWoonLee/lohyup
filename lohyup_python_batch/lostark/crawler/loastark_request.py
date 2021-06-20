import json

import requests


class LostArkMarketRequestParameter:
    action = "List_v2"
    firstCategory = ''
    secondCategory = ''
    characterClass = ''
    tier = ''
    grade = ''
    itemName = ''
    pageNo = ''
    isInit = ''
    sortType = ''

    def __init__(self, first_category, second_category, character_class, tier, grade, item_name, page_no, is_init,
                 sort_type):
        self.firstCategory = first_category
        self.secondCategory = second_category
        self.characterClass = character_class
        self.tier = tier
        self.grade = grade
        self.itemName = item_name
        self.pageNo = page_no
        self.isInit = is_init
        self.sortType = sort_type

    def get_params(self):
        return {
            "firstCategory": self.firstCategory,
            "secondCategory": self.secondCategory,
            "characterClass": self.characterClass,
            "tier": self.tier,
            "grade": self.grade,
            "itemName": self.itemName,
            "pageNo": self.pageNo,
            "isInit": self.isInit,
            "sortType": self.sortType
        }


class LostArkRequest:
    domain = "https://lostark.game.onstove.com"
    request_parameter = None

    def __init__(self, request_parameter):
        self.request_parameter = request_parameter

    def get(self):
        return requests.get(self.domain, params=self.request_parameter.get_params())


class LostArkMarketRequest(LostArkRequest):
    def __init__(self, request_parameter):
        super().__init__(request_parameter)
        self.domain = f'{super().domain}/Market/{request_parameter.action}'


class LostArkAuctionRequest(LostArkRequest):
    def __init__(self, request_parameter):
        super().__init__(request_parameter)
        self.domain = f'{LostArkRequest.domain}/Auction/{request_parameter.action}'
