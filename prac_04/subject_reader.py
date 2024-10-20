"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data from file and display it with correct format"""
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Read subject data from the file and return it as a list of lists"""
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
    """Display subject info."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))




main()