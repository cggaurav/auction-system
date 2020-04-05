from src.bid import Bid
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

	def is_not_sold(self):
		if self.status == 'UNSOLD':
			return True
		else:
			return False

	def mark_sold(self):
		self.status = 'SOLD';

	def get_number_of_bids(self):
		return len(self.bids)

	def add_bid(self, bid):
		self.bids.append(bid)

	def take_stock(self, time=float('inf')):
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

		if self.is_not_sold() and time >= self.get_auction_end_time():
			if self.get_number_of_bids() > 0:
				# TODO: Check
				self.bids = sorted(self.bids, cmp=compare)

				if self.bids[0].get_bidding_price() >= self.reserved_price():
					self.mark_sold()
			else:
				logging.info('Item has no bids unfortunately and time has passed', self)

	def get_highest_bid_price(self):
		# Assumes, we have already taken stock of the item
		if self.get_number_of_bids() == 0:
			return 0.00
		else:
			return self.bids[0].get_bidding_price()

	def get_lowest_bid_price(self):
		# Assumes, we have already taken stock of the item
		if self.get_number_of_bids() == 0:
			return 0.00
		else:
			return self.bids[-1].get_bidding_price()

	def get_price_paid(self):
		# At the end of the auction the winner will pay the price of the second highest bidder, if there
		# is only a single valid bid they will pay the reserve price of the auction.
		if self.get_number_of_bids() == 0:
			return 0.00
		if self.get_number_of_bids() == 1:
			return self.get_reserved_price()
		else:
			return self.bids[1].get_bidding_price()

	def get_winner(self):
		if self.get_number_of_bids() == 0:
			return ''
		else:
			return self.bids[0].get_bidder_id()