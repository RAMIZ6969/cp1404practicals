from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    fancy_taxi = SilverServiceTaxi("Silver Hummer", 100, 2)

    fancy_taxi.drive(18)
    print(fancy_taxi)
    fare = fancy_taxi.get_fare()
    print(f"Fare: ${fare:.2f}")

    assert abs(fare - 48.78) < 0.01, f"Expected fare: $48.78, but got: ${fare:.2f}"


main()
