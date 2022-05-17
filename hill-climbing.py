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



def atractividad():

    #arreglo que contiene la atractividad de cada comuna de construir
    atractividad = [1.0 / w for w in costoComuna] 
    pesos = sum(atractividad)
    atractividad = [w / pesos for w in atractividad]

    return atractividad




# def hill_climbing (solActual):
#     solActual = greedy.greedy( greedy.generadorMatrizAdyacencia() )
#     pesototal = sum(solActual)
    
#     while(True):
#         solNueva = greedy.greedy( greedy.generadorMatrizAdyacencia() )
#         pesonuevo = sum(solNueva)
#         if pesonuevo < pesototal:
#             solActual = solNueva
#             pesototal = pesonuevo
#         else:
#             break


print (generadorMatrizAdyacencia())