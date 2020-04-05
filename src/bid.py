from src.item import Item

import logging

class Bid:
	# Class Variables
	byUser = {}

	def __init__(self, bidding_time, bidder_id, item_name, bidding_price):
		# eg 17|8|BID|toaster_1|20.00
		self.bidding_time = bidding_time
		self.bidder_id = bidder_id
		self.item_name = item_name
		self.bidding_price = bidding_price

	# A bid is considered valid if it:
	#   * Arrives after the auction start time and before or on the closing time.
	#   * Is larger than any previous valid bids submitted by the user.
	# If two bids are received for the same amount then the earliest bid wins the item.
	def is_valid(self):
		try:
			item = Item.get_by_name(self.item_name)
		except ItemDoesNotExistError:
			logging.error('Item does not exist for this bid')
			return False

	def get_bidder(self):
		return self.bidder_id
