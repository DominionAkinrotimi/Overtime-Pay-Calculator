''' 
QUESTION
    Write an algorithm to calculate and output the overtime pay for 10 employees. Overtime payment is 3000naira per hour for every hour worked over 40 hours per week. Assume that employees do not work for fractional part of an hour 
'''
hours = []
Overtime = []
for hour in range(10):
    hours_worked = int(input(f"hours worked for employee_{hour} = "))
    if hours_worked > 40:
        Overtime_pay = (hours_worked - 40) * 3000
        Overtime.append(Overtime_pay)
    else:
        Overtime_pay = 0
        Overtime.append(Overtime_pay)
    hours.append(hours_worked)
print (f"Overtime pay = {Overtime} Hours_worked = {hours}")
