# Toy Car Workshop
# You work in a toy car workshop, and your job is to build toy cars from a collection of parts. Each toy car needs 4 wheels, 1 car body, and 2 figures of people to be placed inside. Given the total number of wheels, car bodies and figures available, how many complete toy cars can you make?

def cars(wheels, bodies, figures):
	totalCars = False
	while wheels >= 0 and bodies >= 0 and figures >= 0:
		wheels = wheels - 4
		bodies = bodies - 1
		figures = figures - 2
		totalCars = totalCars + 1
	
	return totalCars -1

print(cars(43, 15, 87))

print(cars(88, 37, 17))
print(cars(37, 15, 20))
print(cars(72, 7, 21))