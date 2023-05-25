class ExtendedStack(list):
	
	top1 = 0
	top2 = 0
	
	def sum(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1 + self.top2)

	def sub(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1 - self.top2)

	def mul(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1 * self.top2)

	def div(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1 // self.top2)




 