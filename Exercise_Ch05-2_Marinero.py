#Get input from user
def get_input():
    while True:
        try:
            num_list = [int(input(f"Enter integer {i + 1}: ")) for i in range(6)]
            return num_list
        except ValueError:
            print("Invalid input. Please enter integers only.")

#sum of even numbers
def sum_even(numbers):
    even_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    return even_sum

#sum of odd numbers
def sum_odd(numbers):
    odd_sum = 0

    for num in numbers:
        if num % 2 != 0:
            odd_sum += num

    return odd_sum

#main function
def main():
    while True:
        numbers = get_input()

        even_sum = sum_even(numbers)
        odd_sum = sum_odd(numbers)

        print("Sum of even integers:", even_sum)
        print("Sum of odd integers:", odd_sum)

        repeat = input("Do you want to repeat? (y/n): ").lower()
        if repeat != 'y':
            break

#runs main function 
if __name__ == "__main__":
    main()
