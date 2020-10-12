import math

sin = math.sin
pi  = math.pi

n = raw_input("number")
n = int(n)
def cal(a):
	return int(n*a+n)
for i in range(n+1):
	x = float(i) / n * 2 * pi
	a = sin(x)
	print "#"*cal(a)





	


