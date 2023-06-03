def get_num(task, errortext):
    x = True
    while x:
        try:                                                                         # get a number function
            numf = float(input(task))
            x = False
        except ValueError:
            print(errortext)
        else:
            return numf


def continue_program():
    x = True
    while x:                                                                    # repeat the program function
        contpr = input("Do you wish to enter a new calculation? (Y/N) ")
        if contpr == "y" or contpr == "Y":
            return True
        elif contpr == "N" or contpr == "n":
            return False
        else:
            pass


def oper(n1, n2):
    print("1 - addition\n2 - subtraction\n3 - multiplication\n4 - division\n5 - exponents\n")  #operator
    op = get_num("Pick an operator: ", "Invalid task. ")
    if op == 1:
        print("The result is:", n1 + n2)
    elif op == 2:
        print("The result is:", n1 - n2)
    elif op == 3:
        print("The result is:", n1 * n2)
    elif op == 4:
        div = 0
        try:
            div = n1 / n2
            print("The result is:", div)
        except ZeroDivisionError:
            print("Can not divide by zero.")
    elif op == 5:
        print("The result is:", n1 ** n2)
    else:
        print("Incorrect operator.")


def main():
    print("Welcome to my calculator.")
    cont = True
    while cont:
        n1 = get_num("Enter the first number: ", "Invalid number")
        n2 = get_num("Enter the second number: ", "Invalid number")         #main code
        oper(n1, n2)
        if continue_program():
            pass
        else:
            cont = False
    print("Press Enter.")


main()