"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

state = input("Enter short state: ").upper()
while state != "":
    try:
        print(state, "is", CODE_TO_NAME[state])
    except KeyError:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
