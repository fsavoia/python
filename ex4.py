# The variable "cars" will be 100
cars = 100

# The variable "space_in_a_car" will be 4.0
space_in_a_car = 4.0

# The variable "drivers" will be 30
drivers = 30

# The variable "passengers" will 90
passengers = 90

# The variable "cars_not_driven" will be the result of "cars - drivers"
# 100 (cars) - 30 (drivers) = 70 (cars_not_driven)
cars_not_driven = cars - drivers

# The variable "cars_driven" will be equal to "drivers" variable
# cars_driven = 30 (drivers)
cars_driven = drivers

# The "carpool_capacity" variable will be "cars_driven * space_in_a_car"
# 30 (cars_driven) * 4.0 (space_in_a_car) = 120.0 (carpool_capacity)
carpool_capacity = cars_driven * space_in_a_car

# The "average_passengers_per_car" will be "passengers / cars_driven"
# 90 (passengers) / 30 (cars_driven) = 3 (average_passengers_per_car)
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."
