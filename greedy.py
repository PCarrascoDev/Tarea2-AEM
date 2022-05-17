from ast import Str
from importlib.metadata import distribution
import numpy as np



""" comunasColindantes = [
    [2, 3, 4],
    [1, 4],
    [1, 4, 5, 6],
    [1, 2, 3, 5],
    [3, 4, 6, 7, 8, 9],
    [3, 5, 9],
    [5, 8, 10, 11],
    [5, 7, 9, 10],
    [5, 6, 8, 10, 11],
    [7, 8, 9, 11],
    [7, 9, 10]
]

matAdy = np.zeros((11, 11))

for i in range(11):
    for j in range(len(comunasColindantes[i])):
        matAdy[i][comunasColindantes[i][j]-1] = 1
for i in range(11):
    matAdy[i][i]=1
--------------------------------------------------------------------- """

""" Matriz N x N con las comunas adyacentes para
    cada una de las comunas. La diagonal es de 1's
    por terminos prácticos y considerar la cobertura
    de la misma comuna. """

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
""" Cantidad de comunas que cubriría
    un posible vacunatorio en cada
    una de las comunas. """
coberturas = [4, 3, 5, 5, 7, 4, 5, 5, 6, 5, 4]

""" Costos de construcción para cada
    vacunatorio. """
costos = [60, 30, 60, 70, 130, 50, 70, 60, 50, 80, 40]

""" Relación costo/cobertura para cada
    comuna (MAYOR ES MEJOR). """
ratios = np.empty(11)
for i in range(11):
    ratios[i] = (coberturas[i]/costos[i])
#normalizamos el vector
ratios = np.divide(ratios, np.sum(ratios))

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

""" Suma de los costos por comuna 
    asociados de implementar una solución. """
def totalCost(sol):
    sum = 0
    for i in range(11):
        if sol[i] == 1:
            sum += costos[i]
    return sum


""" Esta función entrega una distribución
    de probabilidades, tomando en cuenta
    los ratios (costo/cobertura), además de
    retroalimentarse con la cantidad de veces
    que se escoge un i como el siguiente i
    en cada iteración. Para ello se almacena
    la frecuencia con la que se escoge cada uno. """
def getDistrib(freq):
    distrib = np.full(11, 1.0/11)
    distrib = np.multiply(distrib, ratios)
    distrib = np.multiply(distrib, freq)
    distrib = np.divide(distrib, np.sum(distrib))
    #print(distrib)
    return distrib




def stochGreedy(L, seed):
    np.random.seed(seed)
    freq = np.ones(11)
    sol_antigua = np.zeros(11)
    for i in range(L):
        sol_nueva = np.zeros(11)
        while(isSol(sol_nueva) == False):
            
            choice = np.random.choice([0,1,2,3,4,5,6,7,8,9,10], 1, p=getDistrib(freq))[0]
            freq[choice] += 1
            sol_nueva[choice] = 1
            
        if(totalCost(sol_nueva) < totalCost(sol_antigua) or totalCost(sol_antigua) == 0):
            sol_antigua = sol_nueva
        else:
            freq = np.ones(11)
    return sol_antigua

#print(np.random.choice([0,1,2,3,4,5,6,7,8,9,10], 1, p=distrib)[0])    

""" #solGen(100000)
solution = stochGreedy(20, 5)
print(solution)
print(totalCost(solution)) """

def __main__():
    print("----------------------------------------------------------------------")
    for i in range(20):
        seed = np.random.randint(100000000)
        iterations = 10
        sol = stochGreedy(iterations, seed)
        print("Seed: " + str(seed) + " Greedy Iterations: " + str(iterations))
        print("Solution set: " + str(sol) + " Solution cost: $" + str(totalCost(sol)) + "M")
        print("----------------------------------------------------------------------")

if __name__ == "__main__":
    __main__()
