import pytest
from src.bid import Bid
from src.item import Item

def test_if_bid_is_valid_for_same_item_and_bidder_within_auction_time():
	# An book that starts auction at 1 and ends at 100, with user 1 wanting to sell it for 10
	item = Item(1, 1, 'book1', 10, 100)

	bid0 = Bid(1, 2, 9, item)
	assert bid0.is_valid(item) == False

	bid1 = Bid(1, 2, 10, item)
	assert bid1.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(2) == 10

	bid2 = Bid(2, 2, 13, item)
	assert bid2.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(2) == 13

	bid3 = Bid(3, 2, 13, item)
	assert bid3.is_valid(item) == True

	assert Bid.get_largest_bid_for_bidder(2) == 13

	bid4 = Bid(4, 2, 15, item)
	assert bid4.is_valid(item) == True


def test_if_bid_is_valid_for_same_item_and_bidder_outside_auction_time():
	# Another book that starts auction at 1 and ends at 100, with user 1 wanting to sell it for 10
	item = Item(1, 1, 'book2', 10, 100)

	bid1 = Bid(100, 3, 11, item)
	assert bid1.is_valid(item) == True

	bid2 = Bid(101, 3, 13, item)
	assert bid2.is_valid(item) == False

