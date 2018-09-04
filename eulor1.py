import sys
def gcd(a,b):
	if a < b:
		a, b = b, a
	 
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a

p=1009
q=3643
c=0
y=(p-1)*(q-1)
print y
for e in range(1,y):
	if gcd(e,y)==1:
		if (gcd(e-1,p-1)+1)*(gcd(e-1,q-1)+1)==9:
			c+=e
print c
