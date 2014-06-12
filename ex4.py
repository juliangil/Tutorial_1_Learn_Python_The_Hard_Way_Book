cars = 100
#start an integer variable with one value of 100

space_in_a_car = 4.0
#start a double variable with one value of 4.0, it´s mean the people capacity in the car

drivers = 30
#the driver are 30, this is a new variable

passengers = 90
#the passengers are 90, again this is a new variable

cars_not_driven = cars - drivers
#this are the cars that haven´t drivers

cars_driven = drivers
#this are the cars that have drivers

carpool_capacity = cars_driven * space_in_a_car
#this is the maximun capacity in the lot the cars, at the moment

average_passengers_per_car = passengers / cars_driven
#promedium the people by car // 90/(los carros que tienen conductor)


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."