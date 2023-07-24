#function that determines rate per hourly wage
def CalPay(hrs, rate):
    if hrs < 0 or rate < 0:
        return None

    if hrs > 60:
        pay_amount = 60 * rate + (hrs - 60) * 2 * rate
    elif hrs > 40:
        pay_amount = 40 * rate + (hrs - 40) * 1.5 * rate
    else:
        pay_amount = hrs * rate

    return pay_amount

#function that receives input from user 
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

#main function that uses while loop 
def main():
    while True:
        hours = get_valid_input("Enter the number of hours worked: ")
        rate = get_valid_input("Enter the hourly rate: ")

        # Calculate pay using the CalPay function
        pay = CalPay(hours, rate)

        if pay is not None:
            print("The pay amount is:", pay)
        else:
            print("Invalid input. Hours worked and hourly rate must be positive numbers.")

        repeat = input("Do you want to repeat? (y/n): ").lower()
        if repeat != 'y':
            break

#main function 
if __name__ == "__main__":
    main()