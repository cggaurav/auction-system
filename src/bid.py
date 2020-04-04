# A bid is considered valid if it:
#   * Arrives after the auction start time and before or on the closing time.
#   * Is larger than any previous valid bids submitted by the user.
# eg 17|8|BID|toaster_1|20.00
class Bid:
    def __init__(self, bidding_time, bidder_id, item_name, bidding_price):
        # TODO Check Item
        self.bidding_time = bid_time
        self.bidder_id = bidder_id
        self.item_name = item_name
        self.bidding_price = bidding_price

    def is_valid(self):
    	pass
