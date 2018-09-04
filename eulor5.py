import itertools
import math
def gcd(a,b):
	if a < b:
		a, b = b, a
	 
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a

  
def getChildren(num,lt):
    isZhishu = True  
    i = 2  
    square = int(math.sqrt(num)) + 1  
    while i <= square:  
        if num % i == 0:  
	            lt.append(i)  
	            isZhishu = False  
	            getChildren(num / i,lt)  
	            i += 1  
	            break  
        i += 1  
    if isZhishu: 
        lt.append(num)  
def phi(number):
	lt=[] 
	getChildren(number,lt)
	lt = list(set(lt))
	if len(lt)==1:
		return number-1  
	for i in range(0,len(lt)):
		number=(number/lt[i])*(lt[i]-1)
	return number

print phi(200)

def g(a,n,b,m):
	r=1
	if (a*m-b*n)%gcd((m-n),m*n)!=0:
		return 0
	mn=m*n
	ss=m-n
	ttt=(a*m-b*n)%mn
	for x in range(1,m * n):
		if (ss*x)%mn==ttt:
			if (x%n==a) and (x%m==b):
				r=0
				return x

	if r==1:
		return 0
print g(3,4,4,6),g(2,4,4,6)
result=0
for i in range(10000,10500):
	print i
	for j in range(10000,i):
		result+=g(phi(i),i,phi(j),j)
print result