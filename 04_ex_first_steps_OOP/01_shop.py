class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = list(items)

    def get_items_count(self):
        return len(self.items)

"""test print"""
# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())