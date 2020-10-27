def calculator():


        print ("---------------------")
        print ("---------------------")
        print ("|||||CALCULATOR||||||")
        print ("---------------------")
        print ("---------------------")

        print ("+ for additon")
        print ("- for sub")
        print ("* for multiplication")

        num1 = (int(input("/nENTER A 1ST NO.::")
        num2 = (int(input('/nEnter a 2nd no.')
        ope = input("enter a operator")

        if ope == "+":
                formula = num1+num2
                print ("sum of two no. is :",formula)
        elif ope == '-':
                formula = num1-num2
                print ('sub of two no. is:',formula)
        elif ope == '*':
                formula = num1 * num2
                print ('multiplication of two no. is :',formula)
        else:
                print ('invalid operator')

calculator()
