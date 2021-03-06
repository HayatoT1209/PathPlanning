# To pass the test, your code should output "Passed All Dictionary Tests!"
# If you get any other error other than the one printed below, google to figure out what you did. Most likely error to encounter is a Key Error (means key doesn't exist in dictionary).
def test(value, answer):
    if value != answer:
        print('Failed - ' + str(value) + ' should be ' + str(answer))
        exit()
print('')
# Create a blank dictionary called employees
employees = {}

# Make the Key the employee number, and the Value their name.
# Key: 0  Value: 'Ryan'
# Key: 1  Value: 'Andre'
# Key: 2  Value: 'Ted'
# Key: 3  Value: 'Alex'
employees[0] = 'Ryan'
employees[1] = 'Andre'
employees[2] = 'Ted'
employees[3] = 'Alex'

# TEST
test(employees[0], 'Ryan')

# Sort the employees in alphabetical order.
sorted_employees = sorted(employees, key=employees.get, reverse=False)
test(sorted_employees[0], 3)
test(sorted_employees[1], 1)
test(sorted_employees[2], 0)
test(sorted_employees[3], 2)


# Pop employee number 2 and store name in "name".
name = employees.pop(2)
test(name, 'Ted')

try: 
    employees[2]
except: 
    print('Passed All Dictionary Tests!')
    exit()
print('Failed Popping employee')

