from lostark.db.property import LostArkDbConfig


class LostMarketArkDAO:
    """
    LostArk 거래소 DAO
    """
    def __init__(self):
        self.db_config = LostArkDbConfig()
        self.connection = self.db_config.get_connection()

    def select_market_item_sequence(self):
        sql = """
        
        """
        return None

    def insert_market_item(self, market_item):
        sql = """
        INSERT INTO MARKET_ITEM (
              NAME
            , YESTERDAY_AVG_PRICE
            , LAST_PRICE
            , LOWEST_PRICE 
            ) 
        VALUES (
              %s
            , %s
            , %s
            , %s
        )
        """
        return None