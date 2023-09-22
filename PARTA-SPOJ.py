def possible(cooks,nP,mid):
	cnt=0
	for i in range(len(cooks)):
		R=cooks[i]
		j=1
		timeTaken=0
		while True:
			if timeTaken+(R*j)<=mid:
				cnt=cnt+1
				timeTaken=timeTaken+(R*j)
				j=j+1
			else:
				break
		if cnt>=nP:
			return True
	return False
def check(cooks,nP):
	lo=0
	hi=((max(cooks))*((nP*(nP+1))//2))
	ans=-1
	while lo<=hi:
		mid=lo+(hi-lo)//2
		if possible(cooks,nP,mid)==True:
			ans=mid
			hi=mid-1
		else:
			lo=mid+1
	return ans
T=int(input())
for i in range(T):
	nP=int(input())
	l=[int(x) for x in input().split( )]
	nC=l[0]
	cooks=l[1:]
	print(check(cooks,nP))