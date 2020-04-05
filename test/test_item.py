import pytest

from src.item import Item

def test_item_gets_with_no_bids():
	item = Item(1, 1, 'book1', 10.35, 100)

	assert item.get_name() == 'book1'
	assert item.get_auction_start_time() == 1
	assert item.get_auction_end_time() == 100
	assert item.get_status() == 'UNSOLD'
	assert item.is_not_sold() == True
	assert item.get_reserved_price() == 10.35
	assert item.get_number_of_bids() == 0
	assert item.get_highest_bid_price() == 0
	assert item.get_lowest_bid_price() == 0
	assert item.get_price_paid() == 0
	assert item.get_winner() == ''

	item.set_as_sold()
	assert item.get_status() == 'SOLD'
	assert item.is_not_sold() == False