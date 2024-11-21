"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car  # Adjust path as needed if `prac_06` is your folder

def main():
    """Demo test code to show how to use the Car class."""
    # Create a car object named "My Car" with 180 units of fuel
    my_car = Car("My Car", 180)
    my_car.travel(30)
    print(f"{my_car.name} has fuel: {my_car.fuel_amount}")
    print(my_car)  # Displaying the car using the __str__ method

    # Create a new Car object named "Limo" initialized with 100 units of fuel
    limo = Car("Limo", 100)
    limo.refuel(20)  # Add 20 more units of fuel
    print(f"{limo.name} fuel after adding 20 units: {limo.fuel_amount}")  # Check the fuel amount

    # Attempt to drive "Limo" for 115 km
    limo.travel(115)
    print(limo)  # Display the car to check __str__ output

# Run the main function
main()
