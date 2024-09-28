MIN_PASSWORD_LENGTH = 8

password = input(f"Please enter a password (minimum length is {MIN_PASSWORD_LENGTH} characters): ")

while len(password) < MIN_PASSWORD_LENGTH:
    print(f"Error: Password must be at least {MIN_PASSWORD_LENGTH} characters long. Please try again.")
    password = input(f"Please enter a password (minimum length is {MIN_PASSWORD_LENGTH} characters): ")

print("Password accepted.")
