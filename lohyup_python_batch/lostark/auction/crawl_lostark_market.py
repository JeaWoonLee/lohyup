from lostark.crawler.https_crawler import post_https_doc
from lostark.crawler.loastark_request import LostArkMarketRequest, LostArkMarketRequestParameter


def crawl_lostark_market_batch():
    response = get_market_response()

    print(response.text)
    print(response.url)
    print(response.headers)


def get_market_response():
    lostark_request_parameter = LostArkMarketRequestParameter(
        first_category=90000,
        second_category=90200,
        character_class='',
        tier=0,
        grade=99,
        item_name='',
        page_no=2,
        is_init=False,
        sort_type=7
    )
    lostark_market_request = LostArkMarketRequest(lostark_request_parameter)
    return lostark_market_request.get()
