import names
import random
from random import randint
from datetime import date, timedelta
from randomtimestamp import randomtimestamp


job_title_list = ["Manager", "Salesperson", "Engineer", "Secretary"]
manager_id_list = [90001, 90002, 90003, 90004, 90005, 90006]


# def create_emp_data_set(rows):
#     data_list = []

#     for x in range(rows):
#         employee_name = names.get_full_name()
#         job_title = job_title_list[random.randint(0, 3)]
#         manager_id = manager_id_list[random.randint(0, 5)]
#         date_hired = randomtimestamp(text=False).strftime("%d/%m/%Y")
#         salary = random.randint(10000, 25000)
#         department_id = random.randint(1, 4)
#         data_list.append({'Employee ID': x+1,
#                           'Employee Name': employee_name, 'Job Title': job_title, 'Manager ID': manager_id, 'Date Hired': date_hired, 'Salary': salary, 'Department ID': department_id})

#     return data_list


departments = [
    {'Department ID': 1, 'Department Name': "Management", 'Location': "London"},
    {'Department ID': 2, 'Department Name': "Engineering",
     'Location': "Cardiff"},
    {'Department ID': 3, 'Department Name': "Research & Development",
     'Location': "Edinburgh"},
    {'Department ID': 4, 'Department Name': "Sales", 'Location': "Belfast"}
]


def get_department_by_id(departments, id):
    return [department for department in departments if department['Department ID'] == id]


def get_department_by_location(departments, location):
    return [department for department in departments if department['Location'] == location]


def get_employees_by_department(employees, department_id):
    return [employee for employee in employees if employee['Department ID'] == department_id]


def generate_department_report(employees, department_id):
    employees_by_department = get_employees_by_department(
        employees, department_id)

    newList = []
    for employee in employees_by_department:
        newList.append({'Employee ID': employee['Employee ID'],
                        'Employee Name': employee['Employee Name'], 'Job Title': employee['Job Title'], 'Salary': employee['Salary']})

    return newList


def generate_location_report(employees, location):
    department = get_department_by_location(departments, location)[0]
    employees_by_location = get_employees_by_department(
        employees, department['Department ID'])

    newList = []
    for employee in employees_by_location:
        newList.append({'Employee ID': employee['Employee ID'],
                        'Employee Name': employee['Employee Name'], 'Job Title': employee['Job Title'],
                        'Salary': employee['Salary'], 'Department Name': department['Department Name']})

    return newList


def generate_full_report(employees):
    departments_keyed_by_id = {1: get_department_by_id(departments, 1)[0],
                               2: get_department_by_id(departments, 2)[0],
                               3: get_department_by_id(departments, 3)[0],
                               4: get_department_by_id(departments, 4)[0]}

    newList = []
    for employee in employees:
        employee_department_id = employee['Department ID']

        department = {}
        if employee_department_id in departments_keyed_by_id.keys():
            department = departments_keyed_by_id[employee_department_id]
        else:
            department = {'Department ID': employee_department_id,
                          'Department Name': '',
                          'Location': ''
                          }

        newList.append({'Employee ID': employee['Employee ID'],
                        'Employee Name': employee['Employee Name'],
                        'Job Title': employee['Job Title'],
                        'Manager ID': employee['Manager ID'],
                        'Salary': employee['Salary'],
                        'Department ID': department['Department ID'],
                        'Department Name': department['Department Name'],
                        'Location': department['Location']})

    return newList
