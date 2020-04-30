import pytest
from src.auction import Auction
from src.item import Item

def test_auction_with_multiple_items_no_bids():
	auction = Auction()
	auction.processSell(['1', '1', 'SELL', 'toaster_1', '10.00', '20'])
	auction.processSell(['2', '1', 'SELL', 'toaster_2', '10.00', '20'])
	auction.processSell(['3', '1', 'SELL', 'toaster_3', '10.00', '20'])
	
	assert len(auction.get_items()) == 3

	auction.processSell(['4', '1', 'SELL', 'toaster_3', '10.00', '20'])

	assert len(auction.get_items()) == 3

	assert auction.item_exists('toaster_3') == True
	assert auction.item_exists('toaster_30') == False

	assert auction.get_item_by_name('toaster_3') is not None
	assert auction.get_item_by_name('toaster_30') == None


def test_auction_with_single_item_multiple_bids():
	auction = Auction()
	auction.processSell(['1', '1', 'SELL', 'toaster_1', '10.00', '10'])
	assert len(auction.get_items()) == 1

	# timestamp, user_id, action, item_name, price
	auction.processBid(['1', '71', 'BID', 'toaster_1', '1.50'])
	auction.processBid(['2', '71', 'BID', 'toaster_1', '8.50'])
	auction.processBid(['3', '71', 'BID', 'toaster_1', '9.50'])
	auction.processBid(['4', '72', 'BID', 'toaster_1', '10.50'])
	auction.processBid(['5', '72', 'BID', 'toaster_1', '111111.50'])
	auction.processBid(['6', '73', 'BID', 'toaster_1', '9.50'])
	auction.processBid(['7', '74', 'BID', 'toaster_1', '8.50'])
	auction.processBid(['9', '75', 'BID', 'toaster_1', '6.50'])
	auction.processBid(['10', '71', 'BID', 'toaster_1', '5.50'])

	auction.processBid(['11', '78', 'BID', 'toaster_1', '3.50'])
	auction.processBid(['12', '78', 'BID', 'toaster_1', '27.50'])
	auction.processBid(['80', '75', 'BID', 'toaster_1', '7.50'])

	# Total bidcount here is 8 because 71 user bid a value lower next time.
	assert auction.processOutput() == [['10', 'toaster_1', '72', 'SOLD', '10.50', '8', '111111.50', '1.50']]


def test_auction_with_multiple_items_multiple_bids():
	auction1 = Auction()

	auction1.processSell(['10', '1', 'SELL', 'toaster_1', '10.00', '20'])

	auction1.processBid(['12', '80', 'BID', 'toaster_1', '7.50'])
	auction1.processBid(['13', '55', 'BID', 'toaster_1', '12.50'])

	auction1.processSell(['15', '80', 'SELL', 'tv_1', '250.00', '21'])

	auction1.processBid(['17', '80', 'BID', 'toaster_1', '20.00'])
	auction1.processBid(['18', '11', 'BID', 'tv_1', '150.00'])
	auction1.processBid(['19', '33', 'BID', 'tv_1', '200.00'])
	auction1.processBid(['21', '33', 'BID', 'tv_1', '300.00'])

	assert auction1.processOutput() == [ 
		['20', 'toaster_1', '80', 'SOLD', '12.50', '3', '20.00', '7.50'],  
		['21', 'tv_1', '33', 'SOLD', '250.00', '3', '300.00', '150.00'] 
	]

	
	