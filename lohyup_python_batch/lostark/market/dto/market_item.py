class MarketItem:
    """거래소 아이템 DTO """

    def __init__(self, item_name, item_no, yesterday_avg_price, last_price, lowest_price):
        self.item_name = item_name
        self.item_no = item_no
        self.yesterday_avg_price = 0 if yesterday_avg_price == '-' else yesterday_avg_price
        self.last_price = 0 if last_price == '-' else last_price
        self.lowest_price = 0 if lowest_price == '-' else lowest_price
        self.batch_id = ""

    def to_string(self):
        return f'아이템번호: {self.item_no}, 아이템이름: {self.item_name}, 전일평균거래가: {self.yesterday_avg_price}, ' \
               f'최근 거래가: {self.last_price}, 최저가: {self.lowest_price}, 배치 ID: {self.batch_id}'
