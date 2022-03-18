def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError
    return dividend / divisor

students = [
    {'name': 'Bob', 'grades': [75,90]},
    {'name': 'Rolf', 'grades': []},
    {'name': 'Jen', 'grades': [100,90]},

]

try: # Runs until it hits an error
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError: # Runs if a ZeroDivisionError is encountered
    print(f"ERROR: {name} has no grades!")
else: # Runs if no error is encountered
    print("-- All student avergages calculated --")
finally: # Always runs
    print("-- End of student average calculation --")