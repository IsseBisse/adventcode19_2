from operator import add

def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	turns = [row.split(",") for row in data]

	return turns

"""
Part 1
"""
def add_coord(wire, coord, distance):
	if coord[0] in wire:
		if coord[1] not in wire[coord[0]]:
			wire[coord[0]][coord[1]] = distance

	else:
		wire[coord[0]] = {coord[1]: distance}

def coord_in_wire(wire, coord):
	if coord[0] in wire and coord[1] in wire[coord[0]]:
		return wire[coord[0]][coord[1]]

	return None

DIRECTION2COORD = {"R": [1, 0],
	"L": [-1, 0],
	"U": [0, 1],
	"D": [0, -1]}

def unwind_wire(turns):
	wire = dict()
	coord = [0, 0]
	total_distance = 0

	for instruction in turns:
		direction = instruction[0]
		distance = int(instruction[1:])

		for i in range(distance):
			coord = list(map(add, coord, DIRECTION2COORD[direction]))
			total_distance += 1
			add_coord(wire, coord, total_distance)

	return wire

def find_intersection(wire, turns):
	intersections = list()
	coord = [0, 0]
	total_distance = 0

	for instruction in turns:
		direction = instruction[0]
		distance = int(instruction[1:])

		for i in range(distance):
			coord = list(map(add, coord, DIRECTION2COORD[direction]))
			total_distance += 1
			
			distance = coord_in_wire(wire, coord)
			if distance is not None:
				intersections.append((coord, distance, total_distance))

	return intersections

def part_one():
	turns = get_data("input.txt")

	wire = unwind_wire(turns[0])
	intersections = find_intersection(wire, turns[1])
	
	min_distance = float('inf')
	for intersect,_,_ in intersections:
		distance = abs(intersect[0]) + abs(intersect[1])

		min_distance = min(min_distance, distance)

	print("Closest intersect is: %d units away" % min_distance)

"""
Part 2
"""
def part_two():
	turns = get_data("input.txt")

	wire = unwind_wire(turns[0])
	intersections = find_intersection(wire, turns[1])
	
	min_distance = float('inf')
	for intersect, first_distance, second_distance in intersections:
		distance = first_distance + second_distance

		min_distance = min(min_distance, distance)

	print("Closest intersect is: %d units away" % min_distance)

if __name__ == '__main__':
	#part_one()
	part_two()