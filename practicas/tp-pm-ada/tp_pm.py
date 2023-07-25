def getBiggestIslandLen(string):

    anterior = string[0]
    dictionary = dict()
    dictionary[anterior] = 1

    for i in range(1,len(string)):
        if string[i] not in dictionary:
            dictionary[string[i]] = 1

        if anterior == string[i]:
                dictionary[string[i]] += 1
        anterior = string[i]
    
    maximo = max(dictionary, key=dictionary.get)
    return (maximo, dictionary[maximo])

def armar_diccionario(string):
    dictionary = dict()

    for i in range(len(string)):
        if string[i] not in dictionary:
            dictionary[string[i]] = 1
        else:
            dictionary[string[i]] += 1
    return dictionary


def isAnagram(string1 , string2):
    
    if len(string1) != len(string2):
        return False

    dict1 = armar_diccionario(string1)
    dict2 = armar_diccionario(string2)
    return dict1 == dict2


def verifyBalancedParentheses(string):
    count = 0
    dictionary = dict()

    for i in range(len(string)):

        if string[i] == "(":

            if "(" not in dictionary:
                dictionary[string[i]] = False
                count += 1
            else:
                dictionary[string[i] + str(count)] = False 
                count += 1

        if string[i] == ")":
            if dictionary != {}:
                if count-1 == 0:
                    del dictionary["("]
                    count -= 1
                else:
                    del dictionary["(" + str(count-1)]
                    count -= 1
            else:
                return False

    if dictionary == {}:
        return True
    else:
        return False

def reduceLen(string):

    new_str = ""
    flag = False
    for i in range(len(string)-1):

        if flag == True:
            flag = False
            continue
        if string[i] != string[i+1]:
            new_str = new_str + string[i]
        else:
            flag = True
    
    if flag is True:
        return new_str
    else:
        new_str = new_str + string[-1]
        return new_str
    
def isContained(String, SubString):

    long_SubString = len(SubString)

    comprobation_array = [False] * long_SubString
    i = 0

    for char in String:
        if char == SubString[i]:
            comprobation_array[i] = True
            i += 1
        if i == long_SubString:
            break
    if comprobation_array.count(True) == long_SubString:
        return True
    else:
        return False

def compute_prefix_function(P, m):
    prefix = [0] * (m + 1)
    k = 0
    for q in range(2, m + 1):
        while k > 0 and P[k - 1] != P[q - 1]:
            k = prefix[k - 1]
        if P[k - 1] == P[q - 1]:
            k = k + 1
        prefix[q] = k
    return prefix

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    prefix = compute_prefix_function(P, m)
    q = 0
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = prefix[q]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            print("Pattern occurs with shift =", i - m + 1)
            q = prefix[q]


def KMPmod(T, P):
    n = len(T)
    m = len(P)
    prefix = compute_prefix_function(P, m)
    q = 0
    list = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = prefix[q]
        if P[q] == T[i]:
            q = q + 1
        if q == m: 
            list.append(i - m + 1)
            q = prefix[q]
    
    print(list)
    new_list = []
    flag = True
    for i in range(len(list)):
        if flag == True:
            if i == len(list)-1:
                new_list.append(list[i])
            elif list[i] + len(P) >= list[i+1]:
                new_list.append(list[i])
                flag = False
        else:
            flag = True
    print(new_list)

