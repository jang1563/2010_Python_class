def derivative( L ):
    a = []
    b = len(L)
    if b<=1:
        return a
    for i in range(b-1):
        e = (b-1-i)*L[i]
        a.append(e)
    return a


print derivative( [ 1, 2, 3 ] )

print derivative( [ 1, 1, 1, 1, 1 ] )

print derivative( [3] )

