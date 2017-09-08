def answer(h,q):
    r=[]
    for ele in q:
        ans = getParent(ele,2**h-1)
        if(ans) : r.append(ans)
        else : r.append(-1)
    print r


def getParent(node,size):
    rank = size
    index = size
    while rank>0:
        leftindex = index - (rank+1)/2
        rightindex = index - 1
        if node==leftindex or node==rightindex :
            return index
        if node<leftindex: index = leftindex
        else:   index = rightindex
        rank = (rank-1)/2


if __name__=='__main__':
    answer(3,[7,3,5,1])
