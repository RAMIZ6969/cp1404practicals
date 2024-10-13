"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Load data from file formatted like: code,lecturer,number_of_students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)
        # print(repr(line))
        line = line.strip()
        parts = line.split(',')
        # print(parts)
        parts[2] = int(parts[2])
        # print(parts)
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display data nicely."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))




main()