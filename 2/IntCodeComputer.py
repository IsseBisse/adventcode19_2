import copy

class IntCodeComputer:

	def __init__(self):
		self.code = list()
		self.p = 0

	def load(self, code):
		self.code = copy.deepcopy(code)
		self.p = 0

	def run(self, input_):
		
		self.code[1] = input_[0]
		self.code[2] = input_[1]

		exit = False
		while not exit:
			exit = self.parse_opcode()

		return self.code[0]

	def parse_opcode(self):

		opcode = self.code[self.p]

		if opcode == 1:
			self.add()

		elif opcode == 2:
			self.mult()

		elif opcode == 99:
			return True

		else:
			raise Exception("Invalid opcode: %d" % opcode) 


	def add(self):
		in_addr1 = self.code[self.p+1]
		in_addr2 = self.code[self.p+2]
		out_addr = self.code[self.p+3]

		self.code[out_addr] = self.code[in_addr1] + self.code[in_addr2]
		self.p += 4

	def mult(self):
		in_addr1 = self.code[self.p+1]
		in_addr2 = self.code[self.p+2]
		out_addr = self.code[self.p+3]

		self.code[out_addr] = self.code[in_addr1] * self.code[in_addr2]
		self.p += 4