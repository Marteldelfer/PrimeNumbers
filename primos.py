def primos(n: int):
    lista = [2]

    for a in range(3, n, 2):
        divisível = False
        for b in lista:
            if a%b == 0:
                divisível = True
                break
        if divisível == False:
            lista.append(a)
    return lista
    
if __name__ == '__main__':
    from time import time
    start = time()
    print(primos(100000))
    print(time() - start)
