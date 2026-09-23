# Brinlee Wilding
# Create a Python program that estimates the cost of a road trip. Your program will ask the user for
# trip information, perform calculations, and display a personalized trip-cost summary.
# Your program should ask the user for:
# • User’s name
# • Destination
# • One-way distance in miles
# • Vehicle miles per gallon
# • Gas price per gallon
# • Number of travelers
# Your program should calculate:
# • Total miles for the round trip
# • Gallons of gas needed
# • Estimated gas cost
# • Estimated cost per traveler
# Display a readable trip summary that includes:
# • The traveler’s name
# • The destination
# • The total estimated cost
# • The estimated cost per traveler


# having the user enter their information
users_name = input("Enter your name: ")
users_destination = input("Enter your destination: ")
users_one_way_distance_in_miles = int(input("Enter One-way distance in miles: "))
users_vehicle_miles_per_gallon = float(input("Enter your vehicles miles per gallon: "))
gas_price_per_gallon = float(input("Enter gas price per gallon: "))
number_of_travelers = int(input("Enter number of travelers: "))


# trip calculations
total_distance = (users_one_way_distance_in_miles * 2)
gallons_of_gas_needed = (total_distance/users_vehicle_miles_per_gallon)
estimated_gas_cost = (gallons_of_gas_needed * gas_price_per_gallon)
cost_per_traveler = (estimated_gas_cost/number_of_travelers)

# trip summary
print("====================================")
print("trip summary".upper())
print("====================================")
print("Traveler: " + users_name)
print("Destination: " + users_destination)
print("Total Round-Trip Miles: " + str(total_distance))
print("Gallons of Gas: " + str(gallons_of_gas_needed))
print(f"Total Estimated Cost: ${estimated_gas_cost:.2f}")
print("Cost per traveler: $" + format(cost_per_traveler, ".2f"))
print("====================================")
print("Have a great trip!")





