def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	return data

"""
Part 1
"""
def part_one():
	data = get_data("input.txt")


"""
Part 2
"""
def part_two():
	data = get_data("input.txt")

if __name__ == '__main__':
	part_one()