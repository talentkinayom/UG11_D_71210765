data = input("Masukkan string : ")

def cekString():
	if data.replace(".","").isnumeric() == True:
		if float(data)%2 == 0:
			print(format(float(data)/2))
		else :
			print(format((round(float(data))+5)/2))
	else:
		print(data[::-1])

cekString()