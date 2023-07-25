def darCambio(cambio , monedas):
    monedas_minimas = float("inf") 
    monedas.sort(reverse=True) # Ordeno las monedas de mayor a menor

    def backtracking(cambio_actual , monedas_actuales):
        nonlocal monedas_minimas

        if cambio_actual == cambio:
            monedas_minimas = min(monedas_minimas , len(monedas_actuales)) 
            return
        
        for moneda_actual in monedas: #Itero las monedas
            if cambio_actual + moneda_actual <= cambio: # Si le sumo la moneda actual y no se pasa
                backtracking(cambio_actual + moneda_actual , monedas_actuales + [moneda_actual])

    backtracking(0 , [])

    if monedas_minimas != float("inf"):
        return monedas_minimas
    else:
        return False
    
def mochila(PesoMax , latas):
    latas_minimas = float("inf")
    latas.sort(reverse=True)
    aux_list = []

    def backtracking(peso_actual , lista_latas , aux_list):
        nonlocal latas_minimas
        

        if peso_actual == PesoMax:
            if len(lista_latas) <= latas_minimas: #Si pongo <= entonces me da todos los resultados que lo maximizan, no solo 1
                aux_list.append(tuple(lista_latas))

            latas_minimas = min(latas_minimas , len(lista_latas)) #Si quito esta linea veo todas las combinaciones
            return 

        for lata in latas:
            if lata + peso_actual <= PesoMax:
                backtracking(lata + peso_actual , lista_latas + [lata] , aux_list)

    backtracking(0 , [] , aux_list)
    return aux_list


def SubsecuenciaCreciente(array):

    def backtracking(subsecuencia_actual , indice):
        nonlocal subsecuencia_maxima
        
        if len(array) == indice:
            if len(subsecuencia_actual) > len(subsecuencia_maxima):
                subsecuencia_maxima = subsecuencia_actual[:]
            return
            
        if subsecuencia_actual == [] or array[indice] > subsecuencia_actual[-1]:
            subsecuencia_actual.append(array[indice]) # Lo agrego porque es creciente 
            backtracking(subsecuencia_actual , indice + 1) # Busco el mayor del que agregué
            subsecuencia_actual.pop() # Ahora lo elimino para hacerlo con el siguiente indice

        backtracking(subsecuencia_actual , indice + 1) # Se encarga de iterar toda la lista

    subsecuencia_maxima = []
    backtracking([] , 0)
    return subsecuencia_maxima

def subconjuntoSuma(numeros , valor):

    def backtracking(indice , val_actual):
        if val_actual == valor:
            return True
        if val_actual > valor or indice >= len(numeros):
            return False
        
        if backtracking(indice + 1 , val_actual + numeros[indice]):
            return True
        
        if backtracking(indice + 1, val_actual):
            return True
        return False


    return backtracking(0 , 0)


def adminActividades(tareas, inicio, fin):

    tareas_ordenadas = sorted(tareas, key=lambda x: x['fin'])
    new_list = []

    for i in range(len(tareas_ordenadas)):

        tarea_actual = tareas_ordenadas[i]
        if tarea_actual["inicio"] >= inicio and tarea_actual["fin"] <= fin:
            if i == 0:
                new_list.append(tarea_actual)
            elif tarea_actual["inicio"] >= new_list[-1]["fin"]:
                new_list.append(tarea_actual)
    return new_list

def buscarPares(vector):

    vector.sort() # Ordeno de menor a mayor
    k = len(vector) - 1
    sum = []

    for i in range(len(vector)//2):
        sum.append(vector[i] + vector[k])
        k -= 1
    return max(sum)

def beneficioMax(PesoMax , latas):

    # La lista de latas tiene la forma: [(P1 , B1) , (P2 , B2) ,..., (Pn , Bn)]
    # Siendo P el peso y B el beneficio
    latas_ordenadas = sorted(latas, key=lambda x: x[1], reverse=True) # Ordeno de mayor a menor segun el beneficio
    peso_actual = 0
    aux_list = []

    for lata in latas_ordenadas:
        if peso_actual + lata[0] > PesoMax:
            continue

        peso_actual = peso_actual + lata[0]
        aux_list.append(lata)
        if peso_actual == PesoMax:
            return aux_list
    
    return aux_list

def median_of_medians(arr):
    if len(arr) <= 5:
        arr.sort()
        return arr[len(arr) // 2]

    medians = []
    i = 0
    while i < len(arr):
        group = arr[i:i + 5]
        group.sort()
        if len(group) % 2 == 0:
            if len(group) > 2:
                median1 = group[len(group) // 2]
                median2 = group[(len(group) // 2)-1]
            else:
                median1 = group[0]
                median2 = group[1]
            median = (median1 + median2) // 2
        else:
            median = group[len(group) // 2]

        medians.append(median)
        i += 5

    pivot = median_of_medians(medians)

    lower = [x for x in arr if x < pivot]
    upper = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    if len(lower) > len(arr) // 2:
        return median_of_medians(lower)
    elif len(lower) + len(middle) > len(arr) // 2:
        return pivot
    else:
        return median_of_medians(upper)

# # Example usage:
# arr = [3, 1, 7, 5, 2, 4, 6]
# result = median_of_medians(arr)
# print("The median is:", result)

# arr = [9, 2, 5, 3, 7, 1, 6, 8, 4]
# result = median_of_medians(arr)
# print("The median is:", result) # Deberia devolver 5

# arr = [10, 12, 9, 8, 11, 15, 7, 5, 13, 4, 14, 6]
# result = median_of_medians(arr)
# print("The median is:", result) # Deberia devolver 10

# arr = [5, 4, 3, 2, 1]
# result = median_of_medians(arr)
# print("The median is:", result) # Deberia devolver 3

def edit_distance_divide_and_conquer(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)

    # Caso base: ambas cadenas son vacías
    if len_s1 == 0 and len_s2 == 0:
        return 0

    # Caso base: una de las cadenas es vacía
    if len_s1 == 0:
        return len_s2
    if len_s2 == 0:
        return len_s1

    # Caso general: ambas cadenas no son vacías
    cost = 0 if s1[-1] == s2[-1] else 1

    # Calcular las distancias considerando las operaciones permitidas
    insert_cost = edit_distance_divide_and_conquer(s1, s2[:-1]) + 1
    delete_cost = edit_distance_divide_and_conquer(s1[:-1], s2) + 1
    substitute_cost = edit_distance_divide_and_conquer(s1[:-1], s2[:-1]) + cost

    # Devolver la distancia mínima
    return min(insert_cost, delete_cost, substitute_cost)

# Ejemplo de uso:
# cadena1 = "casa"
# cadena2 = "calle"
# distancia = edit_distance_divide_and_conquer(cadena1, cadena2)
# print("La distancia entre '{}' y '{}' es: {}".format(cadena1, cadena2, distancia))

def darCambio_PD(cambio , monedas):

    #Armo una matriz que tenga como columnas desde 0 hasta el cambio , y de filas la cantidad de monedas
    m = len(monedas)
    matriz = [[0 for _ in range(cambio+1)] for _ in range(m)]
    
    for i in range(m):
        valor_moneda = monedas[i]
        for j in range(cambio + 1):
            if i == 0:
                matriz[i][j] = j
            elif j < valor_moneda:
                matriz[i][j] = matriz[i-1][j]
            else:
                aux = (j - valor_moneda) 
                val_precalculado = matriz[i][aux]
                matriz[i][j] = min(matriz[i-1][j] , val_precalculado + 1)
    
    resultado = matriz[-1][-1]
    return resultado


# monedas = [1 , 4 , 6]
# cambio = 8
# print(darCambio_PD(cambio , monedas))


def mochila_PD(peso_max , latas):
    class Lata:
        def __init__(self , peso , list = []):
            self.peso = peso
            self.list = list

    #Armo una matriz que tenga como columnas desde 0 hasta el peso_max , y de filas la cantidad de monedas
    m = len(latas)
    matriz = [[0 for _ in range(peso_max+1)] for _ in range(m)]
    
    for i in range(m):
        valor_moneda = latas[i]
        aux_list = []
        for j in range(peso_max + 1):
            if i == 0:
                if j == 0:
                    matriz[i][j] = Lata(j)
                else:
                    new_list = aux_list.copy()
                    aux_list.append(valor_moneda)
                    new_list.append(valor_moneda)
                    matriz[i][j] = Lata(j , new_list)
            elif j < valor_moneda:
                matriz[i][j] = matriz[i-1][j]
            else:
                aux = (j - valor_moneda) 
                val_precalculado = matriz[i][aux].peso
                peso_minimo = min(matriz[i-1][j].peso , val_precalculado + 1)
                if matriz[i-1][j].peso < val_precalculado + 1:
                    new_list = matriz[i-1][j].list.copy()
                else:
                    new_list = matriz[i][aux].list + [valor_moneda]
                matriz[i][j] = Lata(peso_minimo ,new_list)
    
    resultado = matriz[-1][-1].list
    return resultado


# monedas = [1 , 2 , 4 , 6]
# cambio = 8
# print(mochila_PD(cambio , monedas))

class path:
    def __init__(self , value , list = []):
        self.value = value
        self.list = list

def Camino(tabla):

    filas = len(tabla)
    columnas = len(tabla[0])

    # Caso base, lleno la fila y columna 0
    matriz_aux =  [[0 for _ in range(columnas)] for _ in range(filas)]
    matriz_aux[0][0] = path(tabla[0][0] , (0,0))

    # Primero lleno la fila 0
    fila1 = []
    for i in range(1 , filas):
        aux = tabla[0][i] + matriz_aux[0][i-1].value
        fila1.append((0 , i))
        aux_list = fila1.copy()
        matriz_aux[0][i] = path(aux , aux_list)

    # Lleno la columna 0
    columna1 = []
    for j in range(1 , columnas):
        aux = tabla[j][0] + matriz_aux[j-1][0].value
        columna1.append((j , 0))
        aux_list = columna1.copy()
        matriz_aux[j][0] = path(aux , aux_list)

    for i in range(1 , filas):
        for j in range(1 , columnas):
            aux = tabla[i][j] + min(matriz_aux[i][j-1].value , matriz_aux[i-1][j].value)
            if matriz_aux[i][j-1].value < matriz_aux[i-1][j].value: # Si el de la izquierda es menor al de arriba
                aux_list = matriz_aux[i][j-1].list.copy()   # Me quedo con la izquierda
                aux_list.append((i , j))
            else:
                aux_list = matriz_aux[i-1][j].list.copy() # Sino me quedo con el de arriba
                aux_list.append((i , j))
            matriz_aux[i][j] = path(aux , aux_list)
    return matriz_aux

def camino_corto(tabla , destino):
    dynamic_table = Camino(tabla)

    for tuple in destino:
        aux = dynamic_table[tuple[0]][tuple[1]]
        print(f"El camino hasta {tuple} es : {aux.list} y su valor es '{aux.value}'")


# tabla = [
#     [1, 3, 1],
#     [1, 5, 1],
#     [4, 2, 1]
# ]
# destino = [(1 , 2) , (2 , 2)] # Lista de direcciones a donde se quiere llegar
# camino_corto(tabla , destino)


def LCS(string1 , string2):
    string1 = " " + string1
    string2 = " " + string2
    m = len(string1) # filas
    n = len(string2) # columnas
    dynamic_table = [[0 for _ in range(n)] for _ in range(m)]


    for i in range(1,m):
        for j in range(1,n):
            if string1[i] == string2[j]:
                dynamic_table[i][j] = dynamic_table[i-1][j-1] + 1
            else:
                dynamic_table[i][j] = max(dynamic_table[i-1][j], dynamic_table[i][j-1])
    print(dynamic_table)


    result = ""
    i = m - 1
    j = n - 1
    while True:
        
        if string1[i] == string2[j]:
            result = string1[i] + result
            i -= 1
            j -= 1
        elif dynamic_table[i-1][j] > dynamic_table[i][j-1]:
            i -= 1
        else:
            j -= 1
        if i == 0 or j == 0:
            break
    
    return result

# print(LCS("ABCBDAB" , "BDCABA"))



def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    
    print(f"Su mayor ganancia es {r[n]}")
    while n > 0:
        print(f"{s[n]} | " , end="")  
        n -= s[n]  
        
# Ejemplo de uso:
precios = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
tamaño = 8
print_cut_rod_solution(precios, tamaño)
