again = "yes"
while again == "yes":
    number1 = input("Please enter your first number \n")

    if int(number1) <= -100000000000000 or int(number1) >= 100000000000000:
        number1 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your first number \n")

    if int(number1) <= -100000000000000 or int(number1) >= 100000000000000:
        number1 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your first number \n")

    if int(number1) <= -100000000000000 or int(number1) >= 100000000000000:
        print("Please restart the program and try again and select the first number as a number between -100 trillion and 100 trillion (-100000000000000 to 100000000000000)")
        quit()

    number2 = input("Please enter your second number \n")

    if int(number2) <= -100000000000000 or int(number2) >= 100000000000000:
        number2 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your second number \n")

    if int(number2) <= -100000000000000 or int(number2) >= 100000000000000:
        number2 = input("The number you entered is out of range (more than 100 trillion or less than -100 trillion), please reselect your second number \n")

    if int(number2) <= -100000000000000 or int(number2) >= 100000000000000:
        print("Please restart the program and try again and select the second number as a number between -100 trillion and 100 trillion (-100000000000000 to 100000000000000)")
        quit()

    symbol = input("How would like like to combine these numbers (please write one of the following: Multiply, Divide, Subtract, or Add) \n").lower()

    if symbol == "divide" or symbol == "+" or symbol == "/" and number2 == "0":
        question = input("You cannot divide any number by 0, please choose to either change your second number or your symbol (Choose either symbol, number, or both) \n").lower()
        if question == "number":
            number2 = input("Please select a new second number \n")
        else:
            if question == "symbol":
                symbol = input("Please select a new symbol \n")
            else:
                if question == "both":
                    number2 = input("Please select a new second number \n")
                    symbol = input("Please select a new symbol \n")

    if symbol == "divide" or symbol == "+" or symbol == "/" and number2 == "0":
        question = input("You cannot divide any number by 0, please choose to either change your second number or your symbol (Choose either SYMBOL, NUMBER or BOTH) \n").lower()
        if question == "number":
            number2 = input("Please select a new second number \n")
        else:
            if question == "symbol":
                symbol = input("Please select a new symbol \n")
            else:
                if question == "both":
                    number2 = input("Please select a new second number \n")
                    symbol = input("Please select a new symbol \n")

    if symbol == "divide" or symbol == "+" or symbol == "/" and number2 == "0":
        question = input("You cannot divide any number by 0, please choose to either change your second number or your symbol (Choose to change either your SYMBOL, your NUMBER or BOTH VALUES) \n").lower()
        if question == "number":
            number2 = input("Please select a new second number\n")
        else:
            if question == "symbol":
                symbol = input("Please select a new symbol \n")
            else:
                if question == "both":
                    number2 = input("Please select a new second number \n")
                    symbol = input("Please select a new symbol \n")

    if symbol == "divide" or symbol == "+" or symbol == "/" and number2 == "0":
        print("Please restart the program and try again without using 0 as your second number or division as your symbol")
        quit()

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
                                                    print("Please restart the program and try again by using one of the avalible symbols")
                                                    quit()

    again = input("Whould you like to do another calculation? (Please select yes or no) \n").lower()
    if again == "yes":
        continue
    
    else:
        if again == "no":
            rating = input("Thank you for using this calculator, how would you rate this calculator out of 10? \n")
            if int(rating) <= 0:
                rating = input("Your rating is under 1, please reselect an rating out of 10 \n")
                if int(rating) <= 0:
                    rating = input("Your rating is under 1, please reselect an rating out of 10 \n")
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    print("Please come again and use this")
                    print("DONATE TO MY PATREON")
                    print("CREATING A GAME SOON")
                    print("METROIDVANIA CALLED FROZEN TEARS")
                    print("COMING SOON TO STEAM AND KICKSTARTER")
                    quit()
                print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                print("Please come again and use this")
                print("DONATE TO MY PATREON")
                print("CREATING A GAME SOON")
                print("METROIDVANIA CALLED FROZEN TEARS")
                print("COMING SOON TO STEAM AND KICKSTARTER")
                quit()
            else:
                if int(rating) >= 10:
                    print("Thank you again for using this calculator, I really appretiate the support, and thanks for such a positive support, your rating was", rating, "out of 10 :)")
                    print("Please come again and use this")
                    print("DONATE TO MY PATREON")
                    print("CREATING A GAME SOON")
                    print("METROIDVANIA CALLED FROZEN TEARS")
                    print("COMING SOON TO STEAM AND KICKSTARTER")
                    quit()
                else:
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")                        
                    print("Please come again and use this")
                    print("DONATE TO MY PATREON")
                    print("CREATING A GAME SOON")
                    print("METROIDVANIA CALLED FROZEN TEARS")
                    print("COMING SOON TO STEAM AND KICKSTARTER")
                    quit()

        else: 
            again = input("Please enter YES or NO if you would like to do another calculation \n").lower()
            if again == "no":
                rating = input("Thank you for using this calculator, how would you rate this calculator out of 10? \n")
                print("Please come again and use this")
                print("DONATE TO MY PATREON")
                print("CREATING A GAME SOON")
                print("METROIDVANIA CALLED FROZEN TEARS")
                print("COMING SOON TO STEAM AND KICKSTARTER")

                if int(rating) <= 0:
                    rating = input("Your rating is under 1, please reselect an rating out of 10 \n")
                    if int(rating) <= 0:
                        rating = input("Your rating is under 1, please reselect an rating out of 10 \n")
                        print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                        quit()
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    print("Please come again and use this")
                    print("DONATE TO MY PATREON")
                    print("CREATING A GAME SOON")
                    print("METROIDVANIA CALLED FROZEN TEARS")
                    print("COMING SOON TO STEAM AND KICKSTARTER")
                    quit()
                else:
                    if int(rating) >= 10:
                        print("Thank you again for using this calculator, I really appretiate the support, and thanks for such a positive support, your rating was", rating, "out of 10 :)")
                        quit()
                    else:
                        print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                        print("Please come again and use this")
                        print("DONATE TO MY PATREON")
                        print("CREATING A GAME SOON")
                        print("METROIDVANIA CALLED FROZEN TEARS")
                        print("COMING SOON TO STEAM AND KICKSTARTER")
                        quit()
            else:
                print("You have selected an option that was unavaliable, which counts as a no")
                rating = input("Thank you for using this calculator, how would you rate this calculator out of 10? \n")
                if int(rating) <= 0:
                    rating = input("Your rating is under 1, please reselect an rating out of 10 \n")
                    if int(rating) <= 0:
                        rating = input("Your rating is under 1, please reselect an rating out of 10 \n")
                        print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                        quit()
                    print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                    quit()
                else:
                    if int(rating) >= 10:
                        print("Thank you again for using this calculator, I really appretiate the support, and thanks for such a positive support, your rating was", rating, "out of 10 :)")
                        quit()
                    else:
                        print("Thank you again for using this calculator, your rating was", rating, "out of 10")
                        print("Please come again and use this")
                        print("DONATE TO MY PATREON")
                        print("CREATING A GAME SOON")
                        print("METROIDVANIA CALLED FROZEN TEARS")
                        print("COMING SOON TO STEAM AND KICKSTARTER")
                        quit()