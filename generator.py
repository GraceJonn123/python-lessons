#a full programme that introduces a prime number
def isprime(w):
    if w == 1:
        #one is not prime
        return False
    for x in range (2, w):
        if w % x == 0:
            #prime numbers arent divisible by two
            return False
    else:
        return True

def primes(w = 1):
    while (True):
        if isprime(w): yield w
        w += 1
for w in primes():
    if w > 100: break
    #stops looping at 100
    print (w)

