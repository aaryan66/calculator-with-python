print("Welcome to iCalculate");
goon = "Yes"
while goon == "Yes":
    number1 = float(input("First Number: "))
    number2 = float(input("Second Number: "))
    print("Please type D for Division, M for Multiplication, A for addition and S for subtraction")
    print("""Please choose a following operator: 
            1.Division(D)
            2.Multiplication(M)
            3.Addition(A)
            4.Subtraction(S)""")
    choose = input('')
    if choose == 'A':
        calculation = number1 + number2
        print(calculation)
    elif choose == 'S':
        calculation = number1 - number2
        print(calculation)
    elif choose == 'M':
        calculation = number1*number2
        print(calculation)
    elif choose == 'D':
        calculation = number1/number2
        print(calculation)
    else : 
        print('Invalid syntax')
    goon = input('Do you want to goon?')
    if goon == 'No':
        print('Thanks')
print('Thanks for using our calculator')