def is_prime(n: int):
    divisivel = False
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            divisivel = True
            break
    return not divisivel


def find_nth_prime(n: int) -> int:
    lista: list = [2]
    counter: int = 1
    a: int = 3

    while counter <= n:
        a += 1
        divisivel: bool = False
        for i in lista:
            if a % i == 0:
                divisivel = True
                break
        if not divisivel:
            counter += 1
            lista.append(a)
    
    return lista[counter - 1]

def primes_to_n(n: int) -> list:
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

def first_n_primes(n: int) -> list:
    lista = [2]
    counter: int = 1
    a: int = 3

    while counter <= n:
        a += 1
        divisivel: bool = False
        for i in lista:
            if a % i == 0:
                divisivel = True
                break
        if not divisivel:
            counter += 1
            lista.append(a)

    return lista

def main() -> None:
    from time import time
    start = time()
    print(primes_to_n(50_000))
    print(time() - start)
    start = time()
    print(first_n_primes(5_000))
    print(time() - start)
    start = time()
    print(find_nth_prime(5_000))
    print(time() - start)
    

if __name__ == '__main__':
    main()
