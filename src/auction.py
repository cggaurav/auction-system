from src.bid import Bid
from src.item import Item

import logging

# An auction is a facility to sell and buy items through bids
class Auction:

	def __init__(self):
		self.items = []

	def processInput(self, lines):

		commands = lines.strip().split('\n')
		for command in commands:
			command_delimited = command.strip().split('|')

			if len(command_delimited) == 1:
				self.processHeartBeat(command_delimited)
			elif len(command_delimited) == 5 and command_delimited[2] == 'BID':
				self.processBid(command_delimited)
			elif len(command_delimited) == 6 and command_delimited[2] == 'SELL':
				self.processSell(command_delimited)
			else:
				logging.error('Unknown input', command)

	def processHeartBeat(self, command):
		# print('processHeartBeat', command)
		time = int(command[0])
		self.take_stock(time)

	def processBid(self, command):
		# print('processBid', command) # eg ['12', '8', 'BID', 'toaster_1', '7.50']

		bidding_time = command[0]
		bidder_id = command[1]
		item_name = command[3]
		bidding_price = command[4]

		item = self.get_item_by_name(item_name)

		bid = Bid(bidding_time, bidder_id, bidding_price, item)

	def processSell(self, command):
		# print('processSell', command) # eg ['10', '1', 'SELL', 'toaster_1', '10.00', '20']

		auction_start_time = command[0]
		seller_id = command[1]
		item_name = command[3]
		reserved_price = command[4]
		auction_end_time = command[5]

		if not self.item_exists(item_name):

			item = Item(auction_start_time, seller_id, item_name, reserved_price, auction_end_time)

			self.add_item(item)

	def processOutput(self):
		self.take_stock()

		outputs = []
		for item in self.items:
			output = [
				"%s" % item.get_auction_end_time(),
				"%s" % item.get_name(),
				"%s" % item.get_winner(),
				"%s" % item.get_status(),
				"%.2f" % item.get_price_paid(),
				"%s" % item.get_number_of_bids(),
				"%.2f" % item.get_highest_bid_price(),
				"%.2f" % item.get_lowest_bid_price()
			]
			print("|".join(output))
			outputs.append(output)

		return outputs

	def take_stock(self, time=float('inf')):
		for item in self.items:
				item.take_stock(time)

	def add_item(self, item):
		self.items.append(item)

	def get_items(self):
		return self.items

	def get_item_by_name(self, name):
		# Here return should end the function http://www.compciv.org/guides/python/fundamentals/function-definitions/
		item = None
		for i in self.items:
			if i.get_name() == name:
				item = i
				break
		return item

	def item_exists(self, name):
		if self.get_item_by_name(name):
			return True
		else:
			return False



