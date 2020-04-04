# An item has a unique name and reserved price.
# To buy an item, participants must submit bids with
# a price higher than the reserved price.
# eg 10|1|SELL|toaster_1|10.00|20
class Item:
    def __init__(self, auction_start_time, seller_id, name, reserved_price, auction_end_time):
        # TODO: Check if item already exists
        self.name = name
        self.reserved_price = reserved_price
        self.seller_id = seller_id
        self.auction_start_time = auction_start_time
        self.auction_end_time = auction_end_time
        self.bids = []


    # http://effbot.org/pyfaq/how-do-i-get-a-list-of-all-instances-of-a-given-class.htm
    @classmethod
    def name_exists(cls, name):
        pass

    def number_of_bids(self):
        return len(self.bids)

    def reserved_price(self):
        return self.reserved_price

    def is_on_sale(self, time):
        pass


