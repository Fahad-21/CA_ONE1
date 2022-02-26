import unittest

updated_dictionary_list = []
employee_dict = {'StaffID': '', 'LastName': "", "FirstName": '','RegHours':'', 'HourlyRate': '', 'OTMultiple': "", 'TaxCredit': '', 'StandardBand': ''}
hours_dict = {'StaffID': '', 'Date': '','HoursWorked': ''}
def computeAllPayment(employeeFile,hoursFile):
    employee_data = open(employeeFile, 'r')
    for row in employee_data:
        new_employee_row = row.replace('\n', '')
        new_row = new_employee_row.split(' ')
        employee_dict.update({'StaffID': new_row[0]})
        employee_dict.update({'LastName': new_row[1]})
        employee_dict.update({'FirstName': new_row[2]})
        employee_dict.update({'RegHours': new_row[3]})
        employee_dict.update({'HourlyRate': new_row[4]})
        employee_dict.update({'OTMultiple': new_row[5]})
        employee_dict.update({'TaxCredit': new_row[6]})
        employee_dict.update({'StandardBand': new_row[7]})
        updated_dictionary_list.append(employee_dict)
    hour_data = open(hoursFile, 'r')
for row in hour_data:
        new_hour_row = row.replace('\n', '')
        new_row_2 = new_hour_row.split(' ')
        hours_dict.update({'StaffID': new_row_2[0]})
        hours_dict.update({'Date': new_row_2[1]})
        hours_dict.update({'HoursWorked': new_row_2[2]})
        updated_dictionary_list.append(hours_dict)
        employee = Employee()
        employee.computePayment(new_row_2[2], new_row_2[1])
    employee_data.close()
    hour_data.close()
    return updated_dictionary_list
