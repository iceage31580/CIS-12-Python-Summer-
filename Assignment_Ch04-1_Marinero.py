#function that calculates rate 
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

#"main function"
def main():
    try:
        hours = float(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly rate: "))

        # Calculate pay using the CalPay function
        pay = CalPay(hours, rate)

        if pay is not None:
            print("The pay amount is:", pay)
        else:
            print("Invalid input. Hours worked and hourly rate must be positive numbers.")
    except ValueError:
        print("Invalid input. Hours worked and hourly rate must be numerical values.")

#run main function 
if __name__ == "__main__":
    main()
