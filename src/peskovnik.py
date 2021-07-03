from grafi import plot
def g(n):
    if n % 2 == 0:
        return n / 2
    return n + 1

def g_inv(n):
    '''
    Vrne list števil, ki jih g slika v n
    '''
    if n == 2:
        return [4] # da se ne zacikla
    if n % 2 == 0:
        return [n - 1, 2*n]
    return [2*n]

def f(n):
    if n % 2 == 0:
        return n / 2
    return n - 1

def f_inv(n):
    '''
    Vrne list števil, ki jih f slika v n
    '''
    if n == 1:
        return [2] # da se ne zacikla
    if n % 2 == 0:
        return [n + 1, 2*n]
    return [2*n]

plot(7, g_inv, start=2)
plot(7, f_inv, start=1)
