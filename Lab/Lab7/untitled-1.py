remainder = []
list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def deci_to_any(n, rad):
    a1 = n/rad
    r1 = n%float(rad)
    remainder.append(list1[int(r1)])
    while a1 > rad:
        r1 = a1%float(rad)
        a1 /= rad
        remainder.append(list1[int(r1)])
    remainder.append(list1[int(a1%float(rad))])
    remainder.append(list1[(a1/rad)])
    remainder.reverse()
    print "".join(remainder)
    