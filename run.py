import sys
import logging

from src.auction import Auction


def run():
    """
    Bootstraps the application.
    """
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else None
    if input_file_path:
        try:
            input_file = open(input_file_path, mode="r")
        except FileNotFoundError:
            logging.error("No such file: {}".format(input_file_path))

        input_file_commands = input_file.read()
        Auction.processCommands(input_file_commands)
        input_file.close()
    else:
    	logging.error("Give an input file to start off with.")


if __name__ == '__main__':
    run()