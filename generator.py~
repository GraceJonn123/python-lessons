def isprime(w):
    if w == 1:
        return False
    for x in range (2, w):
        if w % x == 0:
            return False
    else:
        return True

def primes(w = 1):
    while (True):
        if isprime(w): yield w
        w += 1
for w in primes():
    if w > 100: break
    print (w)

