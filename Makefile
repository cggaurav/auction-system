run-sample:
	@./bin/auction test/input/input1.txt # @ is for making the command not print to stdout

test:
	pytest

.PHONY: all test clean