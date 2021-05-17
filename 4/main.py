import re

INPUT_RANGE = "138307-654504"

"""
Part 1
"""
def ok_doubles(number):
	matches = re.findall(r"([0-9])\1", str(number))
	return len(matches) > 0

def ok_increasing(number):
	prev = 0
	for char in str(number):
		if int(char) < prev:
			return False

		prev = int(char)

	return True

def part_one():
	start, stop = tuple(int(value) for value in INPUT_RANGE.split("-"))

	valid_numbers = 0
	for number in range(start, stop+1):
		if ok_doubles(number) and ok_increasing(number):
			valid_numbers += 1

	print("%d valid number found" % valid_numbers)

"""
Part 2
"""
def ok_adjacent(number_string, match):
	prev_ind = match.span()[0] - 1
	next_ind = match.span()[1]

	if prev_ind > 0 and number_string[prev_ind] == match.group()[0]:
		return False

	if next_ind < 6 and number_string[next_ind] == match.group()[0]:
		return False

	return True


def ok_exactly_doubles(number):
	if len(re.findall(r"([0-9])\1", str(number))) == 0:
		return False

	ok_double = False
	for match in re.finditer(r"([0-9])\1", str(number)):
		ok_double |= ok_adjacent(str(number), match)

	return ok_double

def part_two():
	start, stop = tuple(int(value) for value in INPUT_RANGE.split("-"))

	valid_numbers = 0
	for number in range(start, stop+1):
		if ok_exactly_doubles(number) and ok_increasing(number):
			valid_numbers += 1

	print("%d valid number found" % valid_numbers)

if __name__ == '__main__':
	part_one()
	part_two()