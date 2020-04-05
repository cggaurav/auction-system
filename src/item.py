from src.bid import Bid

import logging
# An item has a unique name and reserved price.
# To buy an item, participants must submit bids with
# a price higher than the reserved price.
# eg 10|1|SELL|toaster_1|10.00|20
class Item:
    def __init__(self, auction_start_time, seller_id, name, reserved_price, auction_end_time):
        self.name = name
        self.reserved_price = float(reserved_price)
        self.seller_id = int(seller_id)
        self.auction_start_time = int(auction_start_time)
        self.auction_end_time = int(auction_end_time)
        
        # To start off with the item is not sold yet
        self.status = 'UNSOLD'

        # Stores all the valid bids for an item. Even if there is one valid bid, the item will be sold
        self.bids = []

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_reserved_price(self):
        return self.reserved_price

    def get_auction_start_time(self):
        return self.auction_start_time

    def get_auction_end_time(self):
        return self.auction_end_time

    def get_number_of_bids(self):
        return len(self.bids)

    def add_bid(self, bid):
        self.bids.append(bid)

    def is_not_sold(self):
        if self.status == 'UNSOLD':
            return True
        else:
            return False

    def set_as_sold(self):
        self.status = 'SOLD';

    def can_be_sold(self):
        if self.get_number_of_bids() == 0:
            return False
        else:
            from functools import cmp_to_key

            def compare(bid1, bid2):

                if bid1.get_bidding_price() > bid2.get_bidding_price():
                    return -1
                elif bid1.get_bidding_price() == bid2.get_bidding_price():
                    if bid1.get_bidding_time() > bid2.get_bidding_time(): # Note: Won't be equal, as assumed
                        return -1
                    else:
                        return 1
                else:
                    return 1

            # Sort all bids for item based on highest bid price to loweest bid price
            self.bids.sort(key=cmp_to_key(compare))

            # If the highest bid price is greater than the reserved price, item can be sold
            if self.bids[0].get_bidding_price() >= self.get_reserved_price():
                return True
            else:
                return False

    # Take stock of item, to see if it can be sold based on current bids and auction end time
    def take_stock(self, time=float('inf')):

        if self.is_not_sold() and time >= self.get_auction_end_time() and self.can_be_sold():
            self.set_as_sold()

    def get_highest_bid_price(self):
        # Assumes, we have already taken stock of the item
        if self.get_number_of_bids() == 0:
            return 0
        else:
            return self.bids[0].get_bidding_price()

    def get_lowest_bid_price(self):
        # Assumes, we have already taken stock of the item
        if self.get_number_of_bids() == 0:
            return 0
        else:
            return self.bids[-1].get_bidding_price()

    # At the end of the auction the winner will pay the price of the second highest bidder, if there
    # is only a single valid bid they will pay the reserve price of the auction.
    def get_price_paid(self):
        # Assumes, we have already taken stock of the item
        if self.is_not_sold():
            return 0
        else:
            # Here there is just one valid bid greater than or equal to reserved price
            if self.get_number_of_bids() == 1:
                return self.get_reserved_price()
            else:
                # The second highest price here should be the reserved price instead of something lower
                return max(self.get_reserved_price(), self.bids[1].get_bidding_price())

    def get_winner(self):
        if self.is_not_sold():
            return ''
        else:
            return self.bids[0].get_bidder_id()
            