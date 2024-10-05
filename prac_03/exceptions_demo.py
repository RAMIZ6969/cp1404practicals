"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters something that cannot be converted to an integer when prompted
for the numerator or denominator.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator,
since dividing any number by zero is undefined in mathematics.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can modify the code to prevent the possibility of a ZeroDivisionError
by adding a check to ensure that the denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero denominator.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
