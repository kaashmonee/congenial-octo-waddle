X=0
def newMethod():
	for var in range (20):
		with open ("document.txt","w") as f:
			if (X%2)==0:
				f.write("even"+"\n")
				X+=1
			else:
				f.write("odd"+"\n")
				X+=1

newMethod()