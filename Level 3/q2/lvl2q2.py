def answer(n):
    # your code here
    n = int (n)
    check = { 1 : 0 , 2 : 1 }

    def finder(n):
        if n in check:
            return check[n]
        if n % 2 == 0 : check[n] = finder(n / 2 ) + 1
        else : check[n] = min (finder((n + 1 ) / 2 ) + 2,finder((n - 1 ) / 2 ) + 2 )
        return check[n]
    return finder(n)

for n in range(1, 65):
    print("%s: %s" % (n, answer(n)))
