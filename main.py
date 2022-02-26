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
class Employee():
    all_dict = {'name': '', 'Date': '', 'Regular Hours Worked': '', 'Overtime Hours Worked': '', 'Regular Rate': '', 'Overtime Rate': '', 'Regular Pay': '', 'Overtime Pay': '', 'Gross Pay': '', 'Standard Rate Pay': '', 'Higher Rate Pay': '', 'Standard Tax': '', 'Higher Tax': '', 'Total Tax': '', 'Tax Credit': '', 'Net Deductions': '', 'Net Pay': ''}
 # to compute total payment details
    def computePayment(self,HoursWorked, date):
        self.all_dict.update({'name': employee_dict.get('FirstName') + ' ' + employee_dict.get('LastName')})
        overtime_hors_worked = (int(hours_dict.get('HoursWorked'))) - (int(employee_dict.get('RegHours')))
        hours_worked = int(hours_dict.get('HoursWorked'))
        regular_hours_worked = int(employee_dict.get('RegHours'))
        if regular_hours_worked < hours_worked:
 self.all_dict.update({'Date': date, 'Regular Hours Worked': regular_hours_worked, 'Overtime Hours Worked': overtime_hors_worked, 'Regular Rate': employee_dict.get('HourlyRate')})
        else:
            print('regular hours worked must be less than hours worked')
overtime_rate = int(employee_dict.get('HourlyRate')) + round(((int(hours_dict.get('HoursWorked'))) - (int(employee_dict.get('RegHours')))) * (float(employee_dict.get('OTMultiple'))))
        self.all_dict.update({'Overtime Rate': overtime_rate})
        overtime_pay = overtime_hors_worked * overtime_rate # calculating overtime pay
        regular_pay = int(employee_dict.get('HourlyRate')) * int(employee_dict.get('RegHours'))
        if overtime_pay > 0 and overtime_hors_worked >= 0:
            self.all_dict.update({'Regular Pay': regular_pay})
            self.all_dict.update({'Overtime Pay': overtime_pay})
else:
            print('overtimee hours worked and overtime pay cannot be negative')
        gross_pay = regular_pay + overtime_pay  # to calculate gross pay
        standard_rate_pay = int(employee_dict.get('StandardBand'))
        higher_rate_pay = gross_pay - int(standard_rate_pay)
        standard_tax = (standard_rate_pay * 20) / 100
        higher_tax = (higher_rate_pay * 40) / 100
        total_tax = standard_tax + higher_tax  # to calculate total tax
        tax_credit = int(employee_dict.get('TaxCredit'))
        net_deductions = round(total_tax - tax_credit, 2)  # calculating net_decuction
        net_pay = gross_pay - net_deductions  # calculating net pay
        if net_pay <= gross_pay and net_pay > 0:
