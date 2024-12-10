class CarShowroom:

	def __init__(self):
		self.gst = 0.28
		self.insurance = 30000
		self.fp = self.select()
		if self.fp  != -1:
			print(f"Price of the car : {self.fp}")

	def final_price(self, price):
		fp = price + int(self.gst * price) + self.insurance
		return fp

	def select(self):
		print("""Select any one
			1. Toyota
			2. BMW
			3. Audi""")
		chosen = int(input())
		if chosen == 1:
			return self.toyota()
		elif chosen == 2:
			return self.bmw()
		elif chosen == 3:
			return self.audi()
		else:
			print("invalid choice")
			return -1

	def toyota(self):
		print("""Select any one
			1. Toyota Innova
			2. Toyota Fortuner""")
		chosen = int(input())
		if chosen == 1:
			return self.final_price(1900000)
		elif chosen == 2:
			return self.final_price(3400000)

	def bmw(self):
		print("""Select any one
			1. BMW M5
			2. BMW 7 Series""")
		chosen = int(input())
		if chosen == 1:
			return self.final_price(19900000)
		elif chosen == 2:
			return self.final_price(18200000)

	def audi(self):
		print("""Select any one
			1. Audi Q7
			2. Audi A4""")
		chosen = int(input())
		if chosen == 1:
			return self.final_price(8900000)
		elif chosen == 2:
			return self.final_price(4700000)
while True:
	CarShowroom()