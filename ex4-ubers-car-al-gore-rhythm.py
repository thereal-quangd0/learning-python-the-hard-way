# variables
numOfCars = 100
numOfSeatsPerCar = 4
numOfDrivers = 30
numOfPassengers = 90

# maths
numOfLeftOverCars = numOfCars - numOfDrivers
carsDriven = numOfDrivers

numOfCarPoolPeople = carsDriven * numOfSeatsPerCar
avgPassengersPerCar = numOfPassengers / carsDriven

# words
print "There's approximately", numOfCars, "cars available."
print "There are only", numOfDrivers, "available."
print "There will be", numOfLeftOverCars, "left over cars today"
print "We can transport", numOfCarPoolPeople, "people today."
print "We have", numOfPassengers, "to carpool today."
print "We need to put about", avgPassengersPerCar, "in each car."