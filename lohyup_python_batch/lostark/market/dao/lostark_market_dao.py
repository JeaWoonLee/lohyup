from lostark.db.property import LostArkDbConfig


class LostArkMarketDAO:
    """
    LostArk 거래소 DAO
    """
    def __init__(self):
        self.db_config = LostArkDbConfig()
        self.connection = self.db_config.get_connection()

    def execute_one(self, sql, args=None):
        if args is None:
            args = []
        curs = self.connection.cursor()
        curs.execute(sql, args=args)
        row = curs.fetchone()
        return row

    def commit(self):
        self.connection.commit()
        pass

    def select_market_batch_sequence(self):
        sql = """
        SELECT FN_NEXT_VAL('MARKET_BATCH') AS MARKET_SEQUENCE FROM DUAL;
        """
        rows = self.execute_one(sql)
        return rows[0].__str__()

    def inset_market_batch(self, batch_id):
        sql = """
        INSERT INTO MARKET_BATCH (BATCH_ID, BATCH_DATE) VALUES (%s, SYSDATE())
        """
        self.execute_one(sql, [batch_id])
        pass

    def update_market_batch_success(self, batch_id):
        sql = """
        UPDATE MARKET_BATCH SET IS_SUCCESS = true WHERE BATCH_ID = %s
        """
        self.execute_one(sql, [batch_id])
        pass

    def update_market_batch_fail(self, batch_id):
        sql = """
        UPDATE MARKET_BATCH SET IS_SUCCESS = false WHERE BATCH_ID = %s
        """
        self.execute_one(sql, [batch_id])
        pass

    def insert_item(self, item):
        sql = """
        INSERT INTO ITEM (
              ITEM_NO
            , ITEM_NAME
            , FIRST_CATEGORY_NO
            , SECOND_CATEGORY_NO
            ) 
        VALUES (
              %s
            , %s
            , %s
            , %s
        )
        """
        args = [item.item_no, item.name, item.first_category_no, item.second_category_no]
        self.execute_one(sql, args)
        pass

    def insert_market_item(self, market_item):
        sql = """
        INSERT INTO MARKET_ITEM (
              ITEM_NO
            , ITEM_NAME
            , YESTERDAY_AVG_PRICE
            , LAST_PRICE
            , LOWEST_PRICE 
            , BATCH_ID
            ) 
        VALUES (
              %s
            , %s
            , %s
            , %s
            , %s
            , %s
        )
        """
        args = [market_item.item_no,
                market_item.item_name,
                market_item.yesterday_avg_price,
                market_item.last_price,
                market_item.lowest_price,
                market_item.batch_id
                ]

        self.execute_one(sql, args)
        pass
