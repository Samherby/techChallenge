import names
import random
import string
from random import randint
from datetime import date, timedelta
from randomtimestamp import randomtimestamp

job_title_list = ["Manager", "Salesperson", "Engineer", "Secretary"]
manager_id_list = [90001, 90002, 90003, 90004, 90005, 90006]


def manipulate_data(chance_to_change, normal_value, bad_value):
    if random.randint(1, 100) < chance_to_change:
        return bad_value
    return normal_value


def generate_string(length):
    return ''.join(random.choices(
        string.ascii_lowercase, k=length))


def generate_number(length):
    return ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=length))


def generate_alphanumeric(length):
    return ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=length))


def produce_bad_character():
    choice = random.randint(1, 3)
    if choice == 1:
        return ''
    if choice == 2:
        return generate_string(55)
    if choice == 3:
        return generate_alphanumeric(10)


def produce_bad_number(max_length, is_mandatory):
    lower = 2
    if is_mandatory:
        lower = 1
    choice = random.randint(lower, 3)
    if choice == 1:
        return ''
    if choice == 2:
        return generate_number(max_length+1)
    if choice == 3:
        return generate_alphanumeric(max_length)


def produce_bad_date():
    choice = random.randint(1, 3)
    if choice == 1:
        return ''
    if choice == 2:
        return generate_string(10)
    if choice == 3:
        return generate_alphanumeric(10)


def create_emp_data_set(rows, is_good_data):
    data_list = []
    chance_to_change = 50

    if (is_good_data):
        chance_to_change = 0

    for x in range(rows):
        employee_id = manipulate_data(
            chance_to_change, x+1, produce_bad_number(10, True))

        employee_name = manipulate_data(
            chance_to_change, names.get_full_name(), produce_bad_character())

        job_title = manipulate_data(
            chance_to_change, job_title_list[random.randint(0, 3)], produce_bad_character())

        manager_id = manipulate_data(chance_to_change, manager_id_list[random.randint(
            0, 5)], produce_bad_number(10, False))

        date_hired = manipulate_data(chance_to_change, randomtimestamp(
            text=False).strftime("%d/%m/%Y"), produce_bad_date())

        salary = manipulate_data(
            chance_to_change, random.randint(10000, 25000), produce_bad_number(10, True))

        department_id = manipulate_data(
            chance_to_change, random.randint(1, 4), produce_bad_number(5, True))

        data_list.append({'Employee ID': employee_id,
                          'Employee Name': employee_name, 'Job Title': job_title, 'Manager ID': manager_id, 'Date Hired': date_hired, 'Salary': salary, 'Department ID': department_id})

    return data_list
