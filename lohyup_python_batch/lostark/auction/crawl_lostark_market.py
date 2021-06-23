import pymysql as pymysql

from lostark.crawler.loastark_request import LostArkMarketRequest, LostArkMarketRequestParameter
from lostark.crawler.parser.market_parser import MarketHtmlParser
from lostark.crawler.request.parameters.first_category import FirstCategory
from lostark.crawler.request.parameters.second_category import SecondCategory


class LostArkMarketCrawler:
    """ LostArk 거래소 Crawler

    거래소 재료 아이템 데이터를 크롤링하여 DB에 적재
    """
    def run(self):
        self.crawl_lostark_market_batch()

    @classmethod
    def crawl_lostark_market_batch(cls):
        db_connection = cls.get_db_connection()
        # market_item_list = cls.lostark_market_crawl()
        #
        # for market_item in market_item_list:
        #     print(market_item.to_string())

    @classmethod
    def lostark_market_crawl(cls):
        """ 로스트아크 마켓 크롤링
        :return: MarketItem 배열
        """
        result_list = []
        # 거래소 목록조회 Get Parameter
        parameter_list = cls.get_market_parameter_list()
        for parameter in parameter_list:
            # 페이지 번호 순서대로 요청
            page_no = 1
            while 1:
                parameter.pageNo = page_no

                # HTML Response
                response = cls.get_market_response(parameter)
                # HTML Parser
                market_parser = MarketHtmlParser(response.text)

                # 조회결과가 존재하지 않으면 해당 카테고리 조회 종료
                if not market_parser.is_item_list_exist():
                    break
                else:
                    # 거래소 아이템 목록 추출
                    market_item_list = market_parser.get_item_list()
                    result_list += market_item_list
                    page_no += 1

        return result_list

    @classmethod
    def get_market_parameter_list(cls):
        """크롤링 대상 Parameter List 추출

        :return: LostArkMarketRequestParameter 배열
        """
        parameter_list = []
        for first_category in FirstCategory:
            for second_category in SecondCategory:

                if first_category.value < second_category.value < first_category.value + 10000:
                    parameter = LostArkMarketRequestParameter(
                        first_category=first_category.value,
                        second_category=second_category.value,
                        character_class='',
                        tier=0,
                        grade=99,
                        item_name='',
                        page_no=1,
                        is_init=False,
                        sort_type=7
                    )
                    parameter_list.append(parameter)
        return parameter_list

    @classmethod
    def get_market_response(cls, lostark_request_parameter):
        """LostArk 거래소 목록 Request

        :param lostark_request_parameter: LostArkMarketRequestParameter
        :return: html response
        """
        lostark_market_request = LostArkMarketRequest(lostark_request_parameter)
        return lostark_market_request.get()

    @classmethod
    def get_db_connection(cls):
        conn = pymysql.connect(host="localhost", user="root", password="wpdns1290!", charset="utf8", port=3306)
        curs = conn.cursor()
        sql = "SELECT NOW(), %s, %s FROM DUAL"
        curs.execute(sql, ('A', 'B'))
        rows = curs.fetchall()
        print(rows)
        for row in rows:
            print(row)
        pass
