import csv
from utilities import generate_department_report, generate_location_report, generate_full_report
from test_data import create_emp_data_set


def write_to_file(filename, report, headers):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        for employee in report:
            row = [employee[header] for header in headers]
            writer.writerow(row)


is_good_data = int(input("press 1 for good data, 2 for bad data\n"))
test_sets = int(input("How many test sets would you like to create?:\n"))
rows = int(input("How many employees would you like in each test set?:\n"))
department_id = int(
    input("What department ID would you like to generate this report for?:\n"))
location = input(
    "What location would you like to generate this report for?:\n")


for i in range(test_sets):

    employees = create_emp_data_set(rows, is_good_data == 1)

    department_report = generate_department_report(employees, department_id)
    location_report = generate_location_report(employees, location)
    full_report = generate_full_report(employees)

    write_to_file(f'department_id_Report - {i+1}.csv',
                  department_report, [
                      'Employee ID', 'Employee Name', 'Job Title', 'Salary'])

    write_to_file(f'Department_Location_Report - {i+1}.csv', location_report,
                  [
                      'Employee ID', 'Employee Name', 'Job Title', 'Salary', 'Department Name'])

    write_to_file(f'Full_Report - {i+1}.csv', full_report,
                  ['Employee ID', 'Employee Name',
                   'Job Title', 'Manager ID', 'Salary', 'Department ID', 'Department Name', 'Location'])
