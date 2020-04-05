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