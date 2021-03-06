import pytest

from src.item import Item
from src.bid import Bid

def test_item_gets_with_no_bids():
	# timestamp, user_id, item_name, reserved_price, close time
	item = Item(1, 1, 'item0', 10.35, 100)

	assert item.get_name() == 'item0'
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


def test_item_sale_with_one_bid_below_reserved_price():
	# timestamp, user_id, item_name, reserved_price, close time
	item = Item(1, 1, 'item1', 5.35, 100)

	assert item.get_status() == 'UNSOLD'
	assert item.is_not_sold() == True
	assert item.get_reserved_price() == 5.35

	assert Bid.get_largest_bid_for_bidder(5) == 0
	# bidding_time, bidder_id, bidding_price, item
	bid1 = Bid(1, 5, 5, item)
	assert Bid.get_largest_bid_for_bidder(5) == 5
	assert bid1.is_valid(item) == True
	
	assert item.get_number_of_bids() == 1
	assert item.get_highest_bid_price() == 5
	assert item.get_lowest_bid_price() == 5

	# At the end of the auction
	item.take_stock(101)

	assert item.get_status() == 'UNSOLD'
	assert item.is_not_sold() == True
	assert item.get_price_paid() == 0.00
	assert item.get_winner() == ''
	

def test_item_sale_with_one_bid_above_reserved_price():
	# timestamp, user_id, item_name, reserved_price, close time
	item = Item(1, 1, 'item2', 5.35, 100)

	assert item.get_status() == 'UNSOLD'
	assert item.is_not_sold() == True
	assert item.get_reserved_price() == 5.35

	# bidding_time, bidder_id, bidding_price, item
	bid1 = Bid(1, 10, 9, item)
	assert Bid.get_largest_bid_for_bidder(10) == 9
	assert bid1.is_valid(item) == True

	assert item.get_number_of_bids() == 1

	item.take_stock(50)

	assert item.get_highest_bid_price() == 9
	assert item.get_lowest_bid_price() == 9
	assert item.get_price_paid() == 0
	assert item.get_winner() == ''

	item.take_stock(101)

	assert item.get_highest_bid_price() == 9
	assert item.get_lowest_bid_price() == 9
	assert item.get_price_paid() == 5.35
	assert item.get_winner() == 10
	assert item.get_status() == 'SOLD'
	assert item.is_not_sold() == False


def test_item_sale_with_two_bids():
	# timestamp, user_id, item_name, reserved_price, close time
	item = Item(1, 1, 'item3', 55, 100)

	assert item.get_status() == 'UNSOLD'
	assert item.is_not_sold() == True
	assert item.get_reserved_price() == 55

	# Below reserved price, # bidding_time, bidder_id, bidding_price, item
	bid1 = Bid(1, 30, 10, item)
	assert Bid.get_largest_bid_for_bidder(30) == 10
	assert bid1.is_valid(item) == True

	assert item.get_number_of_bids() == 1

	item.take_stock(50)

	assert item.get_highest_bid_price() == 10
	assert item.get_lowest_bid_price() == 10
	assert item.get_price_paid() == 0
	assert item.get_winner() == ''
	assert item.get_status() == 'UNSOLD'
	assert item.is_not_sold() == True
	
	# Above reserved price, # bidding_time, bidder_id, bidding_price, item
	bid2 = Bid(1, 31, 66, item)
	assert Bid.get_largest_bid_for_bidder(31) == 66
	assert bid2.is_valid(item) == True

	assert item.get_number_of_bids() == 2

	item.take_stock(101)

	assert item.get_highest_bid_price() == 66
	assert item.get_lowest_bid_price() == 10
	assert item.get_price_paid() == 55
	assert item.get_winner() == 31
	assert item.get_status() == 'SOLD'
	assert item.is_not_sold() == False