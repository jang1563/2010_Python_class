import math

sin = math.sin
pi  = math.pi

n = 40
n = int(n)
def cal(a):
	return int((n*a+n)/2+0.5)
for i in range(n+1):
	x = float(i) / n * 2 * pi
	a = sin(x)
	if cal(a)==20:
		print " "*cal(a)+"*"
	elif cal(a)>20 :
		print " "*20+"|"+" "*(cal(a)-20)+"*"
	else:
		print cal(a)*" "+"*"+(20-cal(a)-1)*" "+"|"
	
	

	