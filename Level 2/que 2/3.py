def answer(l):
    r=l[:]
    r.sort()
    sum=0
    for num in r: sum+=num
    rem = sum%3
    ans=0

    if rem==0:
        return form(r)
    elif rem==1:
        for i in r:
            if i%3==1:
                r.remove(i)
                return form(r)
        flag=1
        for i in r:
            if i%3==2:
                r.remove(i)
                if(flag==1): flag+=1
                elif(flag==2): return form(r)
    elif rem==2:
        for i in r:
            if i%3==2:
                r.remove(i)
                return form(r)
        flag=1
        for i in r:
            if i%3==1:
                r.remove(i)
                if(flag==1): flag+=1
                elif(flag==2): return form(r)
    return 0

def form(r):
    ans=0
    r.reverse()
    for i in r:
        ans = ans*10+i
    return ans

if __name__=='__main__':
    print answer([3,1,4,1,5,9])
https://goo.gl/KbDAwo
