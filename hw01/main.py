 for x in range(1,10):
	for k in range(1,x):
		print(end='        ')
	for y in range(x,10):
		print('%d*%d=%3d'%(x,y,x*y),end=' ')
	print("")
