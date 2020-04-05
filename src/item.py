from src.auction import Auction

# An item has a unique name and reserved price.
# To buy an item, participants must submit bids with
# a price higher than the reserved price.
# eg 10|1|SELL|toaster_1|10.00|20
class Item:
    def __init__(self, auction_start_time, seller_id, name, reserved_price, auction_end_time):
        self.name = name
        self.reserved_price = reserved_price
        self.seller_id = seller_id
        self.auction_start_time = auction_start_time
        self.auction_end_time = auction_end_time
        
        self.bids = []
        self.status = 'UNSOLD'

    @classmethod
    def get_by_name(cls, name):
        for item in Auction.items:
            if item.get_name() == name:
                break
            # Here return should end the function http://www.compciv.org/guides/python/fundamentals/function-definitions/
            return item
        return None


    def is_not_duplicated(self, name):
        # TODO
        return True

    def get_name(self):
        return item_name

    def get_number_of_bids(self):
        return len(self.bids)

    def get_reserved_price(self):
        return self.reserved_price

    def is_sold(self, time):
        pass

    def get_highest_bid(self):
        pass

    def get_lowest_bid(self):
        pass

    def get_second_highest_bid(self):
        pass
        # At the end of the auction the winner will pay the price of the second highest bidder, if there
        # is only a single valid bid they will pay the reserve price of the auction. 