MAX_SIZE = 20232
isPrime = []
prime = []
SPF = [];

def mani(N):
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2,N):
        if isPrime[i]:
            prime.append(i)
            SPF[i] = i
        j=0

        while j<len(prime) and i*prime[j]<N and prime[j] <=SPF[i]:
            isPrime[i*prime[j]] = False
            SPF[i*prime[j]] = prime[j]
            j=j+1

def answer(n):
    if n<0 or n>10000:
        return
    N= 20232
    strPrime=""
    for i in range(0,MAX_SIZE):
        isPrime.append(True)
        SPF.append(2)

    mani(N)
    i=0
    while i<len(prime) and prime[i]<=N:
        strPrime = strPrime + str(prime[i])
        i+=1
    return strPrime[n:n+5]

print answer(3)
