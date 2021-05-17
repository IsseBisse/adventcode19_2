import math

def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	fuel = list()
	for line in data:
		fuel.append(int(line))

	return fuel

def fuel_calc(mass):
	return math.floor(mass / 3) - 2

def part_one():
	data = get_data("input.txt")

	fuel_sum = 0
	for mass in data:
		fuel_sum += fuel_calc(mass)

	print(fuel_sum)

def recursive_fuel_calc(mass):
	fuel = math.floor(mass / 3) - 2

	if fuel <= 0:
		return 0

	else:
		return fuel + recursive_fuel_calc(fuel)

def part_two():
	data = get_data("input.txt")

	fuel_sum = 0
	for mass in data:
		fuel_sum += recursive_fuel_calc(mass)

	print(fuel_sum)

if __name__ == '__main__':
	#part_one()
	part_two()