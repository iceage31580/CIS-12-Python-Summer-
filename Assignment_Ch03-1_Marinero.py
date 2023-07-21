# Prompt user for input
def calculate_pay(hours_worked, hourly_rate):
    if hours_worked < 0 or hourly_rate < 0:
        print("You entered the wrong information for hours. ")
        return None

    if hours_worked > 60:
        pay_amount = 60 * hourly_rate + (hours_worked - 60) * 2 * hourly_rate
    elif hours_worked > 40:
        pay_amount = 40 * hourly_rate + (hours_worked - 40) * 1.5 * hourly_rate
    else:
        pay_amount = hours_worked * hourly_rate

    return pay_amount


# Prompt user for input
try:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    # Calculate pay
    pay = calculate_pay(hours, rate)

    if pay is not None:
        print("The pay amount is:", pay)
except ValueError:
    print("You entered the wrong information")