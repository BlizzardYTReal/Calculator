again = "yes"
while again == "yes":
    number1 = input("Please enter your first number \n")
    if int(number1) <= -100000000000000 or int(number1) >= 100000000000000 :
        number1 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your first number \n")
    if int(number1) <= -100000000000000 or int(number1) >= 100000000000000 :
        number1 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your first number \n")
    if int(number1) <= -100000000000000 or int(number1) >= 100000000000000 :
        print("Please restart the program and try again")
        quit()
    number2 = input("Please enter your second number \n")
    if int(number2) <= -100000000000000 or int(number2) >= 100000000000000 :
        number1 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your second number \n")
    if int(number2) <= -100000000000000 or int(number2) >= 100000000000000 :
        number1 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your second number \n")
    if int(number2) <= -100000000000000 or int(number2) >= 100000000000000 :
        print("Please restart the program and try again")
        quit()
    symbol = input("How woud like like to combine these numbers (please write one of the following: Multiply, Divide, Subtract, or Add) \n").lower()

    if symbol == "add" or symbol == "+":
        sum = int(number1) + int(number2)
        print("The sum of your numbers are", sum)

    else:
        if symbol == "subtract" or symbol == "-":
            difference = int(number1) - int(number2)
            print("The difference between your numbers are", difference)

        else:
            if symbol == "multiply" or symbol == "x" or symbol == "*":
                product = int(number1) * int(number2)
                print("The product of your numbers are", product)

            else:
                if symbol == "divide" or symbol == "+" or symbol == "/":
                    quotient = int(number1) / int(number2)
                    print("The quotient of your numbers are", quotient)

                else:
                    newsymbol = input("Your old symbol did not work, please write ONE of the following: Multiply, Divide, Subtract, or Add \n").lower()

                    if newsymbol == "add" or newsymbol == "+":
                        sum = int(number1) + int(number2)
                        print("The sum of your numbers are", sum)
                    else:
                        if newsymbol == "subtract" or newsymbol == "-":
                            difference = int(number1) - int(number2)
                            print("The difference between your numbers are", difference)

                        else:
                            if newsymbol == "multiply" or newsymbol == "x" or newsymbol == "*":
                                product = int(number1) * int(number2)
                                print("The product of your numbers are", product)

                            else:
                                if newsymbol == "divide" or newsymbol == "+" or newsymbol == "/":
                                    quotient = int(number1) / int(number2)
                                    print("The quotient of your numbers are", quotient)

                                else:
                                    newSymbol = input("Your new symbol did not work, please write ONE of the following: Multiply, Divide, Subtract, or Add \n").lower()

                                    if newSymbol == "add" or newSymbol == "+":
                                        sum = int(number1) + int(number2)
                                        print("The sum of your numbers are", sum)

                                    else:
                                        if newSymbol == "subtract" or newSymbol == "-":
                                            difference = int(number1) - int(number2)
                                            print("The difference between your numbers are", difference)
                                        
                                        else:
                                            if newSymbol == "multiply" or newSymbol == "x" or newSymbol == "*":
                                                product = int(number1) * int(number2)
                                                print("The product of your numbers are", product)

                                            else:
                                                if newSymbol == "divide" or newSymbol == "+" or newSymbol == "/":
                                                    quotient = int(number1) / int(number2)
                                                    print("The quotient of your numbers are", quotient)

                                                else:
                                                    print("Please restart the program and try again")
                                                    quit()
    again = input("Whould you like to do another calculation? (Please select yes or no) \n").lower()
    if again == "yes":
        continue
    
    else:
        if again == "no":
            rating = input("Thank you for using this calculator, how would you rate this calculator out of 10? \n")
            if rating <= "0" or rating > "10":
                rating = input("Your rating is under 1 or above 10, please reselect an rating out of 10 \n")
                if rating <= "0" or rating > "10":
                    rating = input("Your rating is under 1 or above 10, please reselect an rating out of 10 \n")
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    quit()
                print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                quit()

            else:
                print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                quit()

        else: 
            again = input("Please enter YES or NO if you would like to do another calculation \n").lower()
            if again == "no":
                rating = input("Thank you for using this calculator, how would you rate this calculator out of 10? \n")

                if rating <= "0" or rating > "10":
                    rating = input("Your rating is under 1 or above 10, please reselect an rating out of 10 \n")
                    if rating <= "0" or rating > "10":
                        rating = input("Your rating is under 1 or above 10, please reselect an rating out of 10 \n")
                        print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                        quit()
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    quit()

                else:
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    quit()
            else:
                print("You have selected an option that was unavaliable, which counts as a no")
                rating = input("Thank you for using this calculator, how would you rate this calculator out of 10? \n")
                if rating <= "0" or rating > "10":
                    rating = input("Your rating is under 1 or above 10, please reselect an rating out of 10 \n")
                    if rating <= "0" or rating > "10":
                        rating = input("Your rating is under 1 or above 10, please reselect an rating out of 10 \n")
                        print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                        quit()
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    quit()
                else:
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    quit()
