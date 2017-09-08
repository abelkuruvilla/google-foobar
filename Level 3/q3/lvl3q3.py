

def rangeXOR(st, end): # inclusive st and exclusive end
    if (end - st) == 0 : return 0
    if (end - st) == 1 : return st
    if (end - st) <= 4 : return reduce ( lambda x, y: x ^ y, range (st, end))
    else :
        begin_range = (st, st / 4 * 4 + 4 )
        end_range = (end / 4 * 4 , end)
        return rangeXOR( * begin_range) ^ rangeXOR( * end_range)

def answer(start, length):
    wlist = [(start + (length - l) * length, start + (length - l) * length + l) for l in range (length, 0 , - 1 )]
    xorReduce = [rangeXOR(start, end) for start, end in wlist]
    return reduce ( lambda x, y: x ^ y, xorReduce)

#
print(answer(0, 3)) #
print(answer(17, 4)) #
print(answer(17, 250)) #
print(answer(17, 2500))
