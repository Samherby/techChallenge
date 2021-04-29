import unittest
from test_data import create_emp_data_set
from utilities import generate_location_report, generate_full_report, generate_department_report
from validation import is_character_valid, is_number_valid


def check_all_employees_match_report_criteria(report, full_report, field_to_check, data_to_check):
    report_ids = [employee['Employee ID'] for employee in report]

    full_report_ids = [employee['Employee ID']
                       for employee in full_report if employee[field_to_check] == data_to_check]

    return report_ids == full_report_ids


def test_validation(report, validation_function, field_to_check, max_length, is_mandatory):
    is_valid = True

    for employee in report:
        if not validation_function(employee[field_to_check], max_length, is_mandatory):
            is_valid = False
    return is_valid


def all_relevant_employees_present(report, full_report, field_to_check, data_to_check):
    all_employees_in_report = len(report)
    all_employees_from_location = len([
        employee for employee in full_report if employee[field_to_check] == data_to_check])

    return all_employees_in_report == all_employees_from_location


class TestLocationReport(unittest.TestCase):
    location = "Cardiff"
    good_employee_data = create_emp_data_set(50, True)
    bad_employee_data = create_emp_data_set(100, False)
    good_location_report = generate_location_report(
        good_employee_data, location)
    bad_location_report = generate_location_report(
        bad_employee_data, location)
    good_full_report = generate_full_report(good_employee_data)
    bad_full_report = generate_full_report(bad_employee_data)

    def test_all_employees_are_from_location(self):
        self.assertTrue(check_all_employees_match_report_criteria(
            self.good_location_report, self.good_full_report, 'Location', self.location))

        self.assertTrue(check_all_employees_match_report_criteria(
            self.bad_location_report, self.bad_full_report, 'Location', self.location))

    def test_all_employees_from_location_are_in_report(self):
        self.assertTrue(all_relevant_employees_present(
            self.good_location_report, self.good_full_report, "Location", self.location))

        self.assertTrue(all_relevant_employees_present(
            self.bad_location_report, self.bad_full_report, "Location", self.location))

    def test_employee_id_validation(self):

        self.assertTrue(test_validation(self.good_location_report,
                                        is_number_valid, "Employee ID", 10, True))

        self.assertTrue(test_validation(self.bad_location_report,
                                        is_number_valid, "Employee ID", 10, True))

    def test_employee_name_validation(self):

        self.assertTrue(test_validation(self.good_location_report,
                                        is_character_valid, "Employee Name", 50, True))

        self.assertTrue(test_validation(self.bad_location_report,
                                        is_character_valid, "Employee Name", 50, True))

    def test_job_title_validation(self):

        self.assertTrue(test_validation(self.good_location_report,
                                        is_character_valid, "Job Title", 50, True))

        self.assertTrue(test_validation(self.bad_location_report,
                                        is_character_valid, "Job Title", 50, True))

    def test_salary_validation(self):

        self.assertTrue(test_validation(self.good_location_report,
                                        is_number_valid, "Salary", 10, True))

        self.assertTrue(test_validation(self.bad_location_report,
                                        is_number_valid, "Salary", 10, True))

    def test_department_name_validation(self):

        self.assertTrue(test_validation(self.good_location_report,
                                        is_character_valid, "Department Name", 50, True))

        self.assertTrue(test_validation(self.bad_location_report,
                                        is_character_valid, "Department Name", 50, True))


class TestDepartmentReport(unittest.TestCase):
    department_id = 4
    good_employee_data = create_emp_data_set(50, True)
    bad_employee_data = create_emp_data_set(100, False)
    good_department_report = generate_department_report(
        good_employee_data, department_id)

    bad_department_report = generate_department_report(
        bad_employee_data, department_id)
    good_full_report = generate_full_report(good_employee_data)
    bad_full_report = generate_full_report(bad_employee_data)

    def test_all_employees_are_from_department(self):
        self.assertTrue(check_all_employees_match_report_criteria(
            self.good_department_report, self.good_full_report, 'Department ID', self.department_id))

        self.assertTrue(check_all_employees_match_report_criteria(
            self.bad_department_report, self.bad_full_report, 'Department ID', self.department_id))

    def test_all_employees_from_department_are_in_report(self):
        self.assertTrue(all_relevant_employees_present(
            self.good_department_report, self.good_full_report, "Department ID", self.department_id))

        self.assertTrue(all_relevant_employees_present(
            self.bad_department_report, self.bad_full_report, "Department ID", self.department_id))

    def test_employee_id_validation_department(self):

        self.assertTrue(test_validation(self.good_department_report,
                                        is_number_valid, "Employee ID", 10, True))

        self.assertTrue(test_validation(self.bad_department_report,
                                        is_number_valid, "Employee ID", 10, True))

    def test_employee_name_validation_department(self):

        self.assertTrue(test_validation(self.good_department_report,
                                        is_character_valid, "Employee Name", 50, True))

        self.assertTrue(test_validation(self.bad_department_report,
                                        is_character_valid, "Employee Name", 50, True))

    def test_job_title_validation_department(self):

        self.assertTrue(test_validation(self.good_department_report,
                                        is_character_valid, "Job Title", 50, True))

        self.assertTrue(test_validation(self.bad_department_report,
                                        is_character_valid, "Job Title", 50, True))

    def test_salary_validation_department(self):

        self.assertTrue(test_validation(self.good_department_report,
                                        is_number_valid, "Salary", 10, True))

        self.assertTrue(test_validation(self.bad_department_report,
                                        is_number_valid, "Salary", 10, True))


if __name__ == '__main__':
    unittest.main()
