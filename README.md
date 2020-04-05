# Auction System

[PROBLEM](PROBLEM.md)

## Getting started

### Build

`make run-sample`

### Test

`make test`

## Assumptions Made

1. Reading from an input file, but printing to stdout only.
2. An item can be sold in an auction only once, that is only the first appearance of 'SELL' for the item is considered and rest ignored.
3. A user can submit a bid for his or her own item.
4. All timestamps move in strictly increasing order
5. A bid can be valid even if the last bid price by the bidder is considered for a different item
6. Two bids don't come at the same time, with the same or a different bidder.
7. A bid is valid even if its bidding price is below the reserved price, however an item will never be sold below the reserved price. If this is the only bid for the item, the highest and lowest bid will be this same value and the bidder needs to pay the reserved price for the item.
8. If there are no bids for an item, the highest and lowest bid price will be 0.00 and not 0
9. If the user bids the same value again, even if if its for the same item, its considered a valid bid.

## Improvements

1. Check if local environment is setup well to run python
2. Break out bidder/seller into a user class
3. Better validation, eg bids are non zero, items names are lowercase for uniqueness, etc

## Notes

### Python Basics

#### On structuring application [link](https://www.kennethreitz.org/essays/repository-structure-and-python)