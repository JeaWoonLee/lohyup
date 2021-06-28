from lostark.crawler.loastark_request import LostArkMarketRequest, LostArkMarketRequestParameter
from lostark.crawler.parser.market_parser import MarketHtmlParser
from lostark.crawler.request.parameters.first_category import FirstCategory
from lostark.crawler.request.parameters.second_category import SecondCategory
from lostark.market.dao.lostark_market_dao import LostArkMarketDAO


class LostArkMarketCrawler:
    """ LostArk 거래소 Crawler

    거래소 재료 아이템 데이터를 크롤링하여 DB에 적재
    """
    batch_id = None

    def run(self):
        self.crawl_lostark_market_batch()

    @classmethod
    def crawl_lostark_market_batch(cls):
        print('crawl_lostark_market_batch 배치 시작')
        # item_list = cls.lostark_item_crawl()
        lostark_market_dao = LostArkMarketDAO()
        batch_id = cls.get_batch_id()
        print(f'배치 ID : {batch_id}')

        try:
            print('LOST_ARK 거래소 아이템 크롤링 시작')
            market_item_list = cls.lostark_market_crawl()
            print(f'LOST_ARK 거래소 아이템 크롤링 결과: {len(market_item_list)} 건')

            print('LOST_ARK 거래소 아이템 크롤링 결과 DB 적재 시작')
            for market_item in market_item_list:
                market_item.batch_id = batch_id
                print(market_item.to_string())
                lostark_market_dao.insert_market_item(market_item)

            print('DB 적재 완료')
            lostark_market_dao.update_market_batch_success(batch_id)
        except Exception as e:
            print('crawl_lostark_market_batch 배치 실행중 오류가 발생하였습니다')
            print(e)
            lostark_market_dao.update_market_batch_fail(batch_id)
        finally:
            lostark_market_dao.commit()
            print('TRANSACTION COMMIT')
            print('crawl_lostark_market_batch 배치 종료')

    @classmethod
    def lostark_item_crawl(cls):
        """ 로스트아크 아이템 크롤링
        :return: Item 배열
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
                    item_list = market_parser.get_item_list(parameter.firstCategory, parameter.secondCategory)
                    result_list += item_list
                    page_no += 1

        return result_list

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
                    market_item_list = market_parser.get_market_item_list()
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
    def get_batch_id(cls):
        lostark_market_dao = LostArkMarketDAO()
        batch_id = lostark_market_dao.select_market_batch_sequence()
        lostark_market_dao.inset_market_batch(batch_id)
        lostark_market_dao.commit()
        return batch_id
