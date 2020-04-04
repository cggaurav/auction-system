from src.bid import Bid
from src.item import Item

class Auction:
    def __init__(self):
        pass

    # http://effbot.org/pyfaq/how-do-i-get-a-list-of-all-instances-of-a-given-class.htm
    @classmethod
    def processCommands(cls, lines):
        commands = lines.split('\n')
        for command in commands:
            cls.processCommand(command)


    @classmethod
    def processCommand(cls, command):

        command_delimited = command.strip().split('|')

        if len(command_delimited) == 1:
            cls.processHeartBeat(command_delimited)
        elif len(command_delimited) == 5 and command_delimited[2] == 'BID':
            cls.processBid(command_delimited)
        elif len(command_delimited) == 6 and command_delimited[2] == 'SELL':
            cls.processSell(command_delimited)
        else:
            pass

    @classmethod
    def processHeartBeat(cls, command):
        print('processHeartBeat', command)
        pass

    @classmethod
    def processBid(cls, command):
        print('processBid', command)
        # ['12', '8', 'BID', 'toaster_1', '7.50']
        bidding_time = int(command[0])
        bidder_id = int(command[1])
        item_name = command[2]
        bidding_price = int(command[3])

        bid = Bid()
        pass

    @classmethod
    def processSell(cls, command):
        print('processSell', command)
        # eg ['10', '1', 'SELL', 'toaster_1', '10.00', '20']
        auction_start_time = int(command[0])
        seller_id = command[1]
        name = command[3]
        reserved_price = float(command[4])
        auction_end_time = int(command[5])

        item = Item(auction_start_time, seller_id, name, reserved_price, auction_end_time)
        print(item.number_of_bids())
        pass




