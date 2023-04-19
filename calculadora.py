print("Welcome to the calculator")
print("To exit type exit")
print("The opprtations is: addition, multi, div, sub")

def calculator(verbose=True):
    firstt = ""

    while True :

        if isinstance(firstt, str): #Si es str entra el if
            firstt = first()
            if firstt == "exit":
                break

        oppp = op()


        if oppp == "exit":
            break

        seecond = second()

        if seecond == "exit":
            break

        firstt = data(oppp, firstt, seecond, verbose=verbose)
        if firstt == "exit":
            break

def first():
    first_number = input ("Insert the first number: ")
    if first_number.lower() == "exit":
        return first_number    
    else:
        error_firstt = error_first(first_number)
        return error_firstt
    
def op():
    opp = input("Insert an operation ")

    if opp.lower() == "exit":
        return opp

    if opp == "addition":
        return opp
    
    elif opp == "multi":
        return opp
    
    elif opp == "sub":
        return opp
    
    elif opp == "div":
        return opp
    
    else:
        print("Operacion no valida.\n Vuelve a intentarlo")
        return op()


def second():
    second_number = input("Insert the second number: ")
    if second_number.lower() == "exit":
        return second_number  
    else:          
        error = error_second(second_number)
        return error


def data(oppp, first_number, second_number, verbose=True):
    
    if oppp.lower() == "addition":
        first_number += second_number
        if verbose:
            print("The result of the addition is:  ", first_number)
            return first_number

    elif oppp.lower() == "multi":
        first_number *= second_number
        if verbose:
            print("The result of the multi is:  ", first_number)
            return first_number

    elif oppp.lower() == "div":


        divv = error_div(first_number, second_number)
        if divv == "exit":
            return divv
        if verbose:
            print("The result of the div is: ", divv)
            return divv

    elif oppp.lower() == "sub":
        first_number -= second_number
        if verbose:
            print("The result of the subtraction is: ", first_number)
            return first_number


    else:
        print("Invalid transaction")
        
    if verbose:
        print(f"The result is: {first_number}")
        
        return first_number


def error_first(first_number):
    try:
        return int(first_number)

    except:
        print("An error has ocurred, you did not enter a number.\n Try again")
        return first()


def error_second(second_number):
    try:
        return int(second_number) 
    
    except:
        print("An error has ocurred, you did not enter a number.\n Try again")
        return second()


def error_div (first_number, second_number):
    try:
        first_number /= second_number
        return first_number
    
    except:
            print("Division by zero is not defined") 
            second_number = second()

            if second_number == "exit":
                return first_number
            
            first_number /= second_number
            return first_number
    
    
if __name__ == '__main__':
    calculator()


        # calculadora
# calculadora
# calculadora
# calculadora
# calculadora
# calculadora
# calculadora
