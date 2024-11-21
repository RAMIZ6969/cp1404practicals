numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]: This expression has a value of 3.
# numbers[-1]: This expression has a value of 2.
# numbers[3]: This expression has a value of 1.
# numbers[:-1]: This expression has values [3, 1, 4, 1, 5, 9]. It is slicing.
# numbers[3:4]: This expression has a value of [1].
# 5 in numbers: The result for this expression is True.
# 7 in numbers: The result for this expression is False.
# "3" in numbers: The result for this expression is False.
# numbers + [6, 5, 3]: This expression has values [3, 1, 4, 1, 5, 9, 2, 6, 5, 3].

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

numbers[0] = "ten"

numbers[-1] = 1

print(numbers[2:])

print(9 in numbers)
