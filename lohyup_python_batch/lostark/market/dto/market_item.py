class MarketItem:
    """거래소 아이템 DTO """

    def __init__(self, name, yesterday_avg_price, last_price, lowest_price):
        self.name = name
        self.yesterday_avg_price = yesterday_avg_price
        self.last_price = last_price
        self.lowest_price = lowest_price

    def to_string(self):
        return f'이름: {self.name}, 전일평균거래가: {self.yesterday_avg_price}, ' \
               f'최근 거래가: {self.last_price}, 최저가: {self.lowest_price}'
