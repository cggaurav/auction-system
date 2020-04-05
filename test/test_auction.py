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

	auction.processBid(['1', '71', 'BID', 'toaster_1', '1.50'])
	auction.processBid(['2', '71', 'BID', 'toaster_1', '8.50'])
	auction.processBid(['3', '71', 'BID', 'toaster_1', '9.50'])
	auction.processBid(['4', '72', 'BID', 'toaster_1', '10.50'])
	auction.processBid(['5', '72', 'BID', 'toaster_1', '111111.50'])
	auction.processBid(['6', '73', 'BID', 'toaster_1', '9.50'])
	auction.processBid(['7', '74', 'BID', 'toaster_1', '8.50'])
	auction.processBid(['8', '75', 'BID', 'toaster_1', '7.50'])
	auction.processBid(['9', '75', 'BID', 'toaster_1', '6.50'])
	auction.processBid(['10', '71', 'BID', 'toaster_1', '5.50'])


	auction.processBid(['11', '78', 'BID', 'toaster_1', '3.50'])
	auction.processBid(['12', '78', 'BID', 'toaster_1', '27.50'])

	assert auction.processOutput() == [['10', 'toaster_1', '72', 'SOLD', '10.50', '8', '111111.50', '1.50']]


	