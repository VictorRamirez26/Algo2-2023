def contiene_suma(A, n):
    A.sort() #O(n logn)
    left = 0
    right = len(A) - 1

    while left < right:
        suma = A[left] + A[right]
        if suma == n:
            return True
        elif suma < n:
            left += 1
        else:
            right -= 1
    return False

#En el peor de sus casos es O(nlogn)
list = [7,3,2,8,5,4,1,6,10,9]
print(contiene_suma(list , 20)) #Caso falso
print(contiene_suma(list,10)) #Caso Verdadero
