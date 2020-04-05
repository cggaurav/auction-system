run-sample:
	./bin/auction test/input/input1.txt

test:
	pytest

.PHONY: all test clean