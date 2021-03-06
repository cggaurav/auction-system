# Auction System [Link](https://gist.github.com/cggaurav/90a5633bfda6eb40ddfc5d9912e0f8ed)

[PROBLEM](PROBLEM.md)

## Getting started

### Run

`make run-sample`

OR

`python run.py {path/to/input_file.txt}`

### Test 

`make test`

## Schema
 
![Schema](https://cdn-std.droplr.net/files/acc_279689/Gy5hLm "Schema" )

## Assumptions Made 

1. An item can be sold in an auction only once, that is only the first appearance of 'SELL' for the item is considered and rest ignored.
2. A user can submit a bid for his or her own item.
3. All timestamps move in strictly increasing order
4. A bid does not come for an uknown item
5. A bid can be valid even if the last bid price by the bidder is considered for a different item, sold or unsold. Similarly, If the user bids the same value again, even if if its for the same item, its considered a valid bid.
6. Two bids don't come at the same time, with the same or a different bidder.
7. A bid is valid even if its bidding price is below the reserved price, however an item will not be sold below the reserved price. If this is the only bid for the item, the highest and lowest bid will be this same value and the item will not be sold.
8. If there are no bids for an item, the highest and lowest bid price will be 0.00 and not 0. In the problem statement, if the item is `UNSOLD` price paid is expected to be `0.00` and the example output actually says `0`.eg `20|tv_1||UNSOLD|0|2|200.00|150.00`
9. Highest and lowest bids will be based on valid bids. eg. If an a invalid bid for item comes, say after auction end time of item , it will not be considered.
10. Number of bids in the output is the number of valid bids.

## Improvements To Make

1. Check if local environment is setup well to run python
2. Currently reading only from an input file and printing to stdout only. Extend IO to read from file or stdin and output to file or stdout.
3. Break out bidder/seller into its own User class, that can manage bids associated with a user.
4. Better validation, eg bids are non zero, items names are lowercase for uniqueness, auction end time is greater than start time, etc
5. Algorithmic Improvements, eg not sorting again when adding a new item to list, but inserting it effeciently

## Notes

### Python Basics

On structuring application [link](https://www.kennethreitz.org/essays/repository-structure-and-python)

On custom sorting [link](https://portingguide.readthedocs.io/en/latest/comparisons.html)

On return values of functions [link](http://www.compciv.org/guides/python/fundamentals/function-definitions/)

Documenting python code [link](https://realpython.com/documenting-python-code/)
