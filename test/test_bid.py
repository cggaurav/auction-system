import pytest
from src.bid import Bid
from src.item import Item

def test_bid_gets():
	# A book that starts auction at 1 and ends at 100, with user 1 wanting to sell it for 10
	item = Item(1, 1, 'book0', 10, 100)

	assert Bid.get_largest_bid_for_bidder(2) == 0

	bid0 = Bid(1, 2, 9, item)

	assert Bid.get_largest_bid_for_bidder(2) == 9

	assert bid0.get_bidding_price() == 9
	assert bid0.get_bidding_time() == 1
	assert bid0.get_bidder_id() == 2

	bid1 = Bid(1, 2, 10, item)

	assert Bid.get_largest_bid_for_bidder(2) == 10


def test_if_bid_is_valid_for_same_item_and_bidder_within_auction_time():
	# Another book that starts auction at 1 and ends at 100, with user 1 wanting to sell it for 10
	item = Item(1, 1, 'book1', 10, 100)

	bid0 = Bid(1, 3, 9, item)
	assert bid0.is_valid(item) == True

	bid1 = Bid(1, 3, 10, item)
	assert bid1.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(3) == 10

	bid2 = Bid(2, 3, 13, item)
	assert bid2.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(3) == 13

	bid3 = Bid(3, 3, 13, item)
	assert bid3.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(3) == 13

	bid4 = Bid(4, 3, 12, item)
	assert bid4.is_valid(item) == False

	assert Bid.get_largest_bid_for_bidder(3) == 13


def test_if_bid_is_valid_for_same_item_and_bidder_outside_auction_time():
	# Another book that starts auction at 1 and ends at 100, with user 1 wanting to sell it for 10
	item = Item(1, 1, 'book2', 10, 100)

	assert Bid.get_largest_bid_for_bidder(4) == 0

	bid0 = Bid(100, 4, 11, item)
	assert bid0.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(4) == 11

	bid1 = Bid(101, 4, 13, item)
	assert bid1.is_valid(item) == False

	assert Bid.get_largest_bid_for_bidder(4) == 11

