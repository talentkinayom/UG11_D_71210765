import random
tipe = input("Masukkan tipe yang ingin anda coba : ")
a = random.randint(1,20)
b = random.randint(1,20)
c = random.randint(1,20)
d = random.randint(1,20)
perbandingan = ["<",">","=="]
x = random.randint(0,2)
pembanding = perbandingan[x]

def generatesoal():
	print("(benar/salah) jika", end=" ")

	if tipe.lower()=="pengurangan":
		print(a,"-",b,pembanding,c,"-",d, sep='')
	elif tipe.lower()=="penjumlahan":
		print(a,"+",b,pembanding,c,"+",d, sep='')
	else:
		print("hanya ada tipe pengurangan/penjumlahan")

generatesoal()
jawaban = input("Masukkan Jawaban Anda: ")


def cekHasil():
	if pembanding == ">" and tipe.lower() == "penjumlahan":
		if ((a+b)>(c+d)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif pembanding == "<" and tipe.lower() == "penjumlahan":
		if ((a+b)<(c+d)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")		
	elif pembanding == ">" and tipe.lower() == "pengurangan":
		if ((a-b)>(c-d)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
	elif pembanding == "<" and tipe.lower() == "pengurangan":
		if ((a-b)<(c-d)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah!")
    

cekHasil()