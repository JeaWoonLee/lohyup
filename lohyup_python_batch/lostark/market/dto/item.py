class Item:
    """거래소 아이템 DTO """

    def __init__(self, item_no, name, first_category_no, second_category_no):
        self.item_no = item_no
        self.name = name
        self.first_category_no = first_category_no
        self.second_category_no = second_category_no
