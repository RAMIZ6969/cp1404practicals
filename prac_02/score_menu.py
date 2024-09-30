def main():
    """Function to control the menu and handle user choices."""

    score = get_valid_score()
    choice = ''

    while choice != 'Q':
        print_menu()
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
        else:
            print("Invalid choice, please try again.")


def print_menu():
    """Function to display the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Function to get a valid score between 0 and 100."""
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score, try again.")
        score = int(input("Enter a valid score (0-100): "))
    return score


def print_result(score):
    """Function to print the result based on the score."""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(f"Result: {result}")


def show_stars(score):
    """Function to print stars equal to the score."""
    print('*' * score)


main()
