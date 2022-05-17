#import greedy
import numpy as np


comunasColindantes = {
    1: [2, 3, 4],
    2: [1, 4],
    3: [1, 4, 5, 6],
    4: [3, 5],
    5: [3, 4, 6, 7, 8, 9],
    6: [3, 5, 9],
    7: [5, 8, 10, 11],
    8: [5, 7, 9, 10],
    9: [5, 6, 8, 10, 11],
    10: [7, 8, 9, 11],
    11: [7, 9, 10]
}

#arreglo que contiene el costo de construir en cada  columna
costoComuna = [60, 30, 60, 70, 130, 50, 70, 60, 50, 80, 40]



#verifica si la solucion es valida
def isSol(sol):
    if sum(sol) == 11:
        return True
    else:
        return False




# Generador de soluciones aleatorias
# (NO ÓPTIMAS)
def solGen(n):
    sol_arr = []
    while(len(sol_arr) < n ):
        sol_arr.append(np.random.binomial(1, 0.5, 11))
        # if isSol(nSol):
        #     sol_arr.append(nSol)
    return sol_arr




def generadorMatrizAdyacencia ():

    #matriz que poseerá la información de las comunas xj colindantes con i
    matrizAdyacencia = np.zeros((11, 11))

    #for que llena la matriz de adyacencia
    for comuna in comunasColindantes:
        for colindante in comunasColindantes[comuna]:
            matrizAdyacencia[comuna - 1][colindante - 1] = 1

    for i in range(11):
        matrizAdyacencia[i-1][i-1] = 1

    return matrizAdyacencia



def atractividad(comuna):
    atractividad = comunasColindantes[comuna]/costoComuna[comuna-1]
    return atractividad



def mejorVecindario(comunas):
    mejorVecindario = 0
    for i in comunas:
        if(atractividad(i) > atractividad(mejorVecindario)):
            mejorVecindario = i
    return mejorVecindario




def hill_climbing (solActual):

    costoTotal = sum(solActual)
    
    while(not isSol(solActual)):
        vecindario = comunasColindantes(solActual)

        for i in vecindario:
            solNueva = solActual.copy()
            solNueva[i] = 0
            costoNuevo = sum(solNueva)
            
            if(costoNuevo < costoTotal):
                solActual = solNueva
                costoTotal = costoNuevo
                break

    return solActual




solActual = solGen(1)[0]
print(solActual)
print (hill_climbing(solActual))
