import numpy
import os

def get_numbers(string):
    list_coef = list()
    broken = string.split()
    global size
    if len(broken) == size:
        for i in broken:
            try:
                numb = float(i)
                list_coef.append(numb)
            except:
                print("\nThere is probably a non numberic character. Try it again")
                get_solution()
    else:
        print("\nThe amount of coefficients is not equal to the quantity of equations(size of the linear system). Try it again")
        get_solution()

    return list_coef

def get_solution():
    list_aux = list()
    aux = 1
    while aux != (size + 1):
        coeficientes = input(f"Coefficients from {aux} equation(separated by space): ")
        all_coef = get_numbers(coeficientes)
        list_aux.append(all_coef)
        aux += 1

    result = input("\nEnter the system's independent coefficients (separated by space): ")
    num_result = get_numbers(result)

    matriz_a = numpy.array(list_aux)
    matriz_b = numpy.array(num_result)

    resp = numpy.linalg.solve(matriz_a, matriz_x)

    return resp

os.system("cls")
size = int(input("\nHow many equations are there in the system: "))
print("\n")
ans = get_solution()
print("\n"+"The vector solution to the system is:\n",ans)
