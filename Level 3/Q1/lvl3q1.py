# import math
# def answer(m,f):
#     m = long(m)
#     f = long(f)
#
#     #if m==f : return "impossible"
#     if m>10**50 or m<1 or f>10**50 or f<1 : return "impossible"
#     step = 0
#     while f>=1 and m>=1 and f!=m:
#
#         # if m>f :
#         #     if m==1 or f==1:m = m - f
#         #     else : m =m - f*math.floor(m/f)
#         # elif f>m :
#         #     if m==1 or f==1:f = f - m
#         #     else : f = f - m*math.floor(f/m)
#         # step+=1
#         if m>f :
#             step +=1+ m/f
#             m = m%f
#
#         elif f>m :
#             step =1+ f/m
#             f = f%m
#
#
#
#     if f==m and f==1: return str(step)
#
#
#     #return "impossible"
#     return str(step)
#

 # solution for problem 2 in level 3
def answer(M, F):
     m = int (M)
     f = int (F)
     if m * f == 0 : return "impossible"
     g = gcd(m, f)
     if g != 1 and abs (m - f) % g == 0 : return "impossible"
     return str (check(m, f))
def check(m, f):
    if m == 1 : return f - 1
    elif f == 1 : return m - 1
    else :
        if m < f: return check(f, m)
        else : return (m / f) + check(m - m / f * f, f)
def gcd(x, y):
    if y == 0 : return x
    else : return gcd(y, x % y)
# print(answer("1", "1")) # print(answer("2", "1")) # print(answer("4", "7")) # print(answer("9", "37")) # print(answer("2", "38")) # print(answer("2978183212347123467888", "8832131497")) # print(answer("0", "100")) # print(answer("9", "9")) # print(answer("0", "0")) # print(answer("1", "1")) # print(answer("2", "2")) # print(answer("12", "9"))




if __name__=='__main__':
    print answer('4','7')
