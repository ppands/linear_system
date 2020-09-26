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
                print("\nAlgum problema foi identificado na entrada dos coeficientes. Tente novamente")
                get_solution()
    else:
        print("\nA quantidade de coeficientes não corresponde a quantidade de variáveis(dimensão do sistema linear). Tente novamente")
        get_solution()

    return list_coef

def get_solution():
    list_aux = list()
    aux = 1
    while aux != (size + 1):
        coeficientes = input(f"Coeficientes da {aux} equação(entre espaços): ")
        all_coef = get_numbers(coeficientes)
        list_aux.append(all_coef)
        aux += 1

    result = input("\nDigite o valores do vetor resultado do sistema(entre espaços): ")
    num_result = get_numbers(result)

    matriz_a = numpy.array(list_aux)
    matriz_x = numpy.array(num_result)

    resp = numpy.linalg.solve(matriz_a, matriz_x)

    return resp

os.system("cls")
size = int(input("\nQuantas equações há no sistema linear: "))
print("\n")
ans = get_solution()
print("\n"+"O vetor resposta para o sistema será:\n",ans)
