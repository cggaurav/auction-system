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

		# Stores all the valid bids for an item
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

	def get_number_of_bids(self):
		return len(self.bids)

	def add_bid(self, bid):
		self.bids.append(bid)

	def take_stock(self, time=float('inf')):
		if item.is_not_sold() and time >= item.get_auction_end_time():
			pass

	def get_highest_bid_price(self):
		pass

	def get_second_highest_bid_price(self):
		pass

	def get_lowest_bid_price(self):
		pass

	def get_winner(self):
		# At the end of the auction the winner will pay the price of the second highest bidder, if there
		# is only a single valid bid they will pay the reserve price of the auction. 
		pass