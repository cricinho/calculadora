print("Biemvemidos a la calculadora")
print("Para salir escribe slir")
print("Las operaciones son: suma, multi, div, resta")

def calculadora(verbose=True):
    first_number = "" 


    while True :
        if isinstance(first_number, str): #Si es str entra el if
            first_number = input ("Ingresa un numero: ")

            if first_number.lower() == "salir":
                break
        
        error_first(first_number)

        first_number = int(first_number)

        op = input("Ingresa una operacion: ")

        if op.lower() == "salir":
            break


        seecond = second()

        datos(op, first_number, seecond, verbose=verbose)

        first_number = datos(op, first_number, seecond)


def second():

    while True:
        second_number = input("Ingresa el segundo numero: ")
        if second_number.lower() == "salir":
            break            
        error = error_second(second_number)
        return error


def datos (op, first_number, second_number, verbose=True):
    
    if op.lower() == "suma":
        first_number += second_number
        if verbose:
            print("El resultado de la suma es :  ", first_number)

    elif op.lower() == "multi":
        first_number *= second_number
        if verbose:
            print("El resultado de la multi es :  ", first_number)

    elif op.lower() == "div":

        try:
            first_number /= second_number

        except:
            print("La division entre cero no esta definida") 
            calculadora()
        
        if verbose:
            print("El resultado de la div es :  ", first_number)

    elif op.lower() == "resta":
        first_number -= second_number
        if verbose:
            print("El resultado de la resta es :  ", first_number)

    else:
        print("Operacion no valida")
        
    if verbose:
        print(f"El resultado es {first_number}")

    return first_number


def error_first(first_number):
    try:
        
        first_number = int(first_number)

    except:
        
        print("Se ha producido un error no ingresaste un numero.\n Vuelve a intentarlo")
        calculadora()


def error_second(second_number):

    try:
        return int(second_number) 
    
    except:
        print("Se ha producido un error no ingresaste un numero \n Vuelve a intentarlo")
        return second()



# def errorop(op):

    # try:
  
        # op = "suma"      
        # op = "multi"
        # op = "div"
        # op = "resta"

    # except:
        # print("No elejiste una operacion")
        # calculadora()

      
















if __name__ == '__main__':
    calculadora()


        