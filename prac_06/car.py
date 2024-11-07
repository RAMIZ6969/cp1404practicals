"""CP1404/CP5632 Practical - Car class example."""

class Car:
    """A class to represent a car."""

    def __init__(self, name="", fuel_amount=0):
        """Initialize a new Car instance with a name and initial fuel amount."""
        self.name = name
        self.fuel_amount = fuel_amount
        self._distance = 0  # this will track the distance the car has traveled

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel_amount}, odometer={self._distance}"

    def refuel(self, extra_fuel):
        """Add extra fuel to the car's current fuel amount."""
        self.fuel_amount += extra_fuel

    def travel(self, distance_km):
        """Drive the car for a given distance if enough fuel is available."""
        if distance_km > self.fuel_amount:
            distance_km = self.fuel_amount
            self.fuel_amount = 0
        else:
            self.fuel_amount -= distance_km
        self._distance += distance_km
        return distance_km
