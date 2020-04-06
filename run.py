import sys

from src.auction import Auction
from src.utils.logger import logger

def run(input_file_commands):
    auction = Auction()

    # Lets start the auction
    auction.processInput(input_file_commands)

    # After auction is completely done
    auction.processOutput()

if __name__ == '__main__':
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else None

    if input_file_path:
        try:
            input_file = open(input_file_path, mode="r")
        except FileNotFoundError:
            logger.error("No such file: {}".format(input_file_path))

        input_file_commands = input_file.read()
        input_file.close()

        run(input_file_commands)
    else:
        logger.error("Give an input file to start off with. `./bin/auction /path/to/inputfile.txt`")
