# Alan
# Practice qns (lab 06)
# to execute a specific line, use ALT+SHIFT+e


# NEW QN
def fly():
    print("The vehicle is in flying mode now!")


class vehicle:
    flight_engine_capacity = "1341 horsepower"

    def __init__(self, number_of_wheels, seating_capacity, food_availability, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.food_availability = food_availability
        self.maximum_velocity = maximum_velocity


Flight1 = vehicle(6, '853', '900', '180')
print(Flight1.number_of_wheels)
print(Flight1.seating_capacity)
print(Flight1.food_availability)
print(Flight1.maximum_velocity)
fly()








dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
tinydict = {name}