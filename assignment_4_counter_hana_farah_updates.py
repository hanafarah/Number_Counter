"""creating a number counter program where if user enter a start value, end value, and step value
Hint: Use a range function
"""
number_counter = input("Hello to Number Counter! To continue, enter any key: ")

"""think of a how a range function operates
"""

while True:
    try:
        start_value = int(input("Enter a start value (Default: 0): "))
        if start_value == 0 or start_value >= 0:
            break
    except ValueError:
        print("Opps! Bad value!")
        print("Please enter a number for the start value.")
        continue

while True:
    try:
        end_value = int(input("Enter a end value: "))
        if end_value == 0 or end_value > 0:
            break
    except ValueError:
        print("Opps! Bad value!")
        print("Please enter a number for the end value.")
        continue

while True:
    try:
        step_value = int(input("Enter a step value (Default: 1): "))
        if step_value == 1 or step_value > 1:
            break
    except ValueError:
        print("Opps! Bad value!")
        print("Please enter a number for the step value.")
        continue

print("The numbers are: ", end=' ')

for value in range(start_value, end_value+step_value, step_value):
    print(value, end=' ')
