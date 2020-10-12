li = [(1,'1',1.0), (2,'2',2.0), (3, '3',3.0)]
print len(li) 
print li[1] 
print li[2][1] 
sum = ""
for i in range(len(li)):
    sum+= li[i][1]

print sum 

"""
3
(2,"2",2.0)
3
123
"""

print 8 in ['Ace', '8']
"""False"""

print "%5s:%.2f%d" %("love",1.413,4)
"""
 love:1.424"""


a = 1.4434325452344

print "%.6f"%(a)


class Point(object):
    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y
    def set(self, x, y):
        self.x = x
        self.y = y
    def get(self):
        return self.x, self.y
    def __str__(self):
        return "%d %d" % (self.x, self.y)
p = Point()
print p 
p.set(3,4)
print p 
print p.get() 

"""
1 2
3 4
(3,4)
"""


f = "love,happy,CS101".split(',')
print "=".join(f)

"""
love=happy=CS101
"""
