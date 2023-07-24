#function that sorts numbers
def sort_numbers(a, b, c, d):
    # Find the smallest number and swap it to the first position
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a

    # Find the second smallest number and swap it to the second position
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b

    # Find the third smallest number and swap it to the third position
    if c > d:
        c, d = d, c

    return a, b, c, d

#main function 
def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))
        d = float(input("Enter the fourth number: "))

        # Call the sort_numbers function to sort the numbers in ascending order
        sorted_numbers = sort_numbers(a, b, c, d)

        print("The numbers in ascending order are:", sorted_numbers)

    except ValueError:
        print("Invalid input. Please enter numerical values for all four numbers.")

#run main
if __name__ == "__main__":
    main()
