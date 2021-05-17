from IntCodeComputer import IntCodeComputer

def get_data(path):
	with open(path) as file:
		data = file.read().split(",")

	data = [int(opcode) for opcode in data]

	return data

def part_one():
	# for i in range(5):
	# 	data = get_data("smallInput%d.txt" % (i+1))

	# 	comp = IntCodeComputer()
	# 	comp.load(data)
	# 	output = comp.run()

	# 	print(output)

	data = get_data("input.txt")

	comp = IntCodeComputer()
	comp.load(data)
	output = comp.run((12,2))

	print(output)

def find_inputs(data):
	comp = IntCodeComputer()

	for noun in range(100):
		for verb in range(100):
			
			comp.load(data)
			
			output = comp.run((noun, verb))

			if output == 19690720:
				return noun, verb


def part_two():
	data = get_data("input.txt")
	
	noun, verb = find_inputs(data)
	print("Noun: %d, verb: %d, product: %d" % (noun, verb, 100*noun+verb))


if __name__ == '__main__':
	#part_one()
	part_two()