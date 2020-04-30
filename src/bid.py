from src.utils.logger import logger

class Bid:
    """An bid belongs to an item, is placed by a bidder with a price and time"""
    bids_by_bidder = {}

    def __init__(self, bidding_time, bidder_id, bidding_price, item):
        self.bidding_time = int(bidding_time)
        self.bidder_id = int(bidder_id)
        self.bidding_price = float(bidding_price)

        if self.is_valid(item):
            self.add_bid_for_bidder(self.get_bidder_id())
            item.add_bid(self)
        else:
            logger.warn('Not a valid bid at {} from {} for {}'.format(self.bidding_time, self.bidder_id, self.bidding_price))
            pass

    def get_bidding_price(self):
        return self.bidding_price

    def get_bidding_time(self):
        return self.bidding_time

    def get_bidder_id(self):
        return self.bidder_id

    def add_bid_for_bidder(self, bidder_id):
        if bidder_id in self.bids_by_bidder:
            Bid.bids_by_bidder[bidder_id].append(self)
        else:
            Bid.bids_by_bidder[bidder_id] = [self]

    @classmethod
    def get_largest_bid_for_bidder(cls, bidder_id):
        from functools import cmp_to_key
        def compare(bid1, bid2):
            if bid1.get_bidding_price() > bid2.get_bidding_price():
                return -1
            elif bid1.get_bidding_price() == bid2.get_bidding_price():
                return 0
            else:
                return 1
        
        if bidder_id in cls.bids_by_bidder:
            return sorted(cls.bids_by_bidder[bidder_id], key=cmp_to_key(compare))[0].get_bidding_price() # Note: Can be improved for performance
        else:
            return 0

    def is_valid(self, item):
        # A bid is considered valid if it:
        #   * Arrives after the auction start time and before or on the closing time.
        #   * Is larger than any previous valid bids submitted by the bidder.
        if (self.get_bidding_time() >= item.get_auction_start_time() and self.get_bidding_time() <= item.get_auction_end_time()) and \
           (self.get_bidding_price() >= self.get_largest_bid_for_bidder(self.get_bidder_id())):
            return True
        else:
            return False
