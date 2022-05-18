#import greedy
import numpy as np
import greedy

MatAdy = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1], 
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
]



""" Generador de soluciones aleatorias
    (NO ÓPTIMAS). Genera un arreglo de
    n soluciones factibles, por prueba
    y error, de forma aleatoria. """
def solGen(n):
    sol_arr = []
    while(len(sol_arr) < n ):
        nSol = np.random.binomial(1, 0.5, 11)
        if isSol(nSol):
            sol_arr.append(nSol)
    return sol_arr



""" Comprueba si una solución es 
    o no factible de a cuerdo a la
    matriz de adyacencia. Una 
    solución es factible si y sólo si
    para cada comuna hay acceso a 
    al menos 1 vacunatorio, ya sea 
    en la misma comuna o en las
    adyacentes. """
def isSol(X):
    sol = True
    for i in range(11):
        sum = 0
        for j in range(11):
            sum += X[j]*MatAdy[i][j]
        if(sum < 1):
            sol = False
            break
    return sol


"""
Función de atractividad, que calcula la atractividad de una construccion
basado en  la cantidad de comunas que se
cubren dividido por el costo de construccion de la comuna.
"""
def atractividad(comuna):
    atractividad = 0
    for i in range(11):
        atractividad += MatAdy[comuna][i]
    atractividad = atractividad / greedy.costos[comuna]
    return atractividad



""""
Compara la atractividad de construir  en cada comuna del 
vecindario de la solución actual según una comuna otorgada
"""
def mejorVecindario(comuna, solActual):
    mejorVecindario = comuna
    for i in range(11):
        if(atractividad( MatAdy[comuna][i] ) > atractividad(mejorVecindario)
            and solActual[i] == 0):
            mejorVecindario = i
    return mejorVecindario



def hill_climbing (solActual):

    solNueva = solActual.copy()

    for i in range(11):
        if(solActual[i] == 1):
            nuevoVacunatorio = mejorVecindario(i, solActual)
            solNueva[i] = 0
            solNueva[nuevoVacunatorio] = 1
            solActual = solNueva.copy()

    return solNueva



def __main__():
    print("----------------------------------------------------------------------")
    solInicial = greedy.stochGreedy(L=10, seed=np.random.randint(100000000))
    print("Solución inicial con Greedy: " +  str(solInicial) + ", costo: " + str(greedy.totalCost(solInicial)))
    solFinal = hill_climbing(solInicial)
    print("Solución con Hill-Climbing: " + str(solFinal) + ", costo: " + str(greedy.totalCost(solFinal)))
    print("----------------------------------------------------------------------")


if __name__ == "__main__":
    __main__()
