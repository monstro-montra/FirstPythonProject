def get_input():  # function for getting input
    while True:  # start a while loop
        try:  # try to execute the following block
            print("Input the first number: ")
            num1 = float(input())
            print("Input the second number: ")
            num2 = float(input())
            return num1, num2
        except ValueError:  # if exception occurs, execute this block. restart the loop
            print("Invalid input, please use a float.")


def main():  # main function
    num1, num2 = get_input()  # get the input
    ans1 = num1 // num2  # integer division
    ans2 = num1 / num2  # float division
    ans3 = num1 % num2  # modulo

    try:  # try the following 
        ans1 = num1 // num2
        print(f"{num1} divided by {num2} equals {ans1} in terms of integer division.")
        print(f"{num1} divided by {num2} equals {ans2} in terms of float division.")
        print(f"{num1} modulo {num2} equals {ans3}.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    main()
