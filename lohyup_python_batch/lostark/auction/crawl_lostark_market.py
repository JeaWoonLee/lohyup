from lostark.crawler.loastark_request import LostArkMarketRequest, LostArkMarketRequestParameter
from lostark.crawler.request.parameters.first_category import FirstCategory
from lostark.crawler.request.parameters.second_category import SecondCategory


def crawl_lostark_market_batch():
    parameter_list = get_market_parameter_list()
    response_list = lostark_market_crawl(parameter_list)

    for response in response_list:
        print(response.text)
        print(response.url)
        print(response.headers)


def get_market_parameter_list():
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


def get_market_response(lostark_request_parameter):
    lostark_market_request = LostArkMarketRequest(lostark_request_parameter)
    return lostark_market_request.get()


def lostark_market_crawl(parameter_list):
    crawl_list = []
    for parameter in parameter_list:
        response = get_market_response(parameter)
        crawl_list.append(response)

    return crawl_list
