import sys
import logging

from src.auction import Auction

def run(input_file_commands):
    # Lets start the auction
    auction = Auction()
    auction.processInput(input_file_commands)

    # After auction is completely done
    auction.processOutput()


if __name__ == '__main__':
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else None

    if input_file_path:
        try:
            input_file = open(input_file_path, mode="r")
        except FileNotFoundError:
            logging.error("No such file: {}".format(input_file_path))

        input_file_commands = input_file.read()
        input_file.close()

        run(input_file_commands)
    else:
        logging.error("Give an input file to start off with.")
