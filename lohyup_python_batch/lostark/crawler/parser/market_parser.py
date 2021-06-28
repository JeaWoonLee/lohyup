import bs4

from lostark.market.dto.item import Item
from lostark.market.dto.market_item import MarketItem


class MarketHtmlParser:
    bs = None

    def __init__(self, html_text=""):
        """ LostArk 거래소 HTML Parser

        :param html_text: 로스트아크 거래소 HTML String
        """
        self.bs = bs4.BeautifulSoup(html_text, 'html.parser')

    def is_item_list_exist(self):
        """ 검색결과 존재여부 체크

        :return: bool
        """
        tbody = self.bs.find('tbody')
        if tbody is None:
            return False

        item_name = tbody.find('span', attrs={'class': 'name'})
        return item_name is not None

    def get_market_item_list(self):
        """거래소 아이템 목록 추출

        :return: 거래소 아이템 목록
        """
        market_item_list = []
        bs_tr_list = self.bs.find('tbody').find_all('tr')

        for bs_tr in bs_tr_list:
            price_list = bs_tr.find_all('div', attrs={'class': 'price'})
            market_item = MarketItem(
                item_name=bs_tr.find('span', attrs={'class': 'name'}).text,
                item_no=bs_tr.find('button').attrs['data-itemno'],
                yesterday_avg_price=price_list[0].find('em').text.replace(',', ''),
                last_price=price_list[1].find('em').text.replace(',', ''),
                lowest_price=price_list[2].find('em').text.replace(',', '')
            )

            market_item_list.append(market_item)

        return market_item_list

    def get_item_list(self, first_category_no, second_category_no):
        """
        아이템 목록 추출
        :return:
        """
        item_list = []
        bs_tr_list = self.bs.find('tbody').find_all('tr')

        for bs_tr in bs_tr_list:
            price_list = bs_tr.find_all('div', attrs={'class': 'price'})
            market_item = Item(
                name=bs_tr.find('span', attrs={'class': 'name'}).text,
                item_no=bs_tr.find('button').attrs['data-itemno'],
                first_category_no=first_category_no,
                second_category_no=second_category_no
            )
            item_list.append(market_item)

        return item_list
