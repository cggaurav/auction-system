# Auction System

[PROBLEM](PROBLEM.md)

## Getting started

### Build

`./bin/auction tests/input/input1.txt`

### Test


## Assumptions Made

1. Reading from FILE, Printing to STDOUT
2. An item can be sold in an auction only once. 
3. Same user can submit a bid for his or her own item.
4. All timestamps move in increasing order
5. A bid can be valid even if the last bid price by the bidder is considered for a different item


## Improvements

1. Binary check if local environment is setup for python 3.x
2. Perhaps we can break out bidder/seller into a user class

## Python Basics 

### On structuring application [link](https://www.kennethreitz.org/essays/repository-structure-and-python)