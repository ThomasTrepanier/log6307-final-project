def par_nepar(n):
    cifre = []

    while n != 0:
        cifre.append(n % 10)
        n //= 10

    even = True
    odd = True
    output = "The number complies to the needed terms"

    for broj in cifre:
        if broj % 2 == 0 and odd:
            even = True
            odd = False
        elif broj % 2 != 0 and even:
            odd = True
            even = False
        else:
            return "The number doesn't comply to the needed terms."
    return output
n = int(input("Unesite broj n: "))
print(par_nepar(n))
