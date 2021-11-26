print("Untuk memulai program masukkan (-1) untuk mulai")
angka1 = int(input(": "))

angka = 0

def tabakangka():
	global angka
	print("Apakah 4?")
	print("Apakah tebakan sudah benar ?")
	print("lebih kecil (0)")
	print("lebih besar (1)")
	print("benar (2)")
	angka2 = int(input(": "))
	angka += 1
	if angka2 == 2:
		print("Jumlah tebakan : ", angka)
		print("Program Selesai !")
	elif angka2 == 0:
		print("Apakah 2?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		angka3 = int(input(": "))
		angka += 1
		if angka3 == 2:
			print("Jumlah tebakan :", angka)
			print("Program Selesai !")
		elif angka3 == 0:
			print("Hasil Penjumlahannya Pasti 1 !")
			angka +=1
			print("Jumlah tebakan :", angka)
			print("Program Selesai !")
	elif angka2 == 1:
		print("Apakah 6?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		angka4 = int(input(": "))
		angka += 1
		if angka4 == 2:
			print("Jumlah tebakan :", angka)
			print("Program Selesai !")
		elif angka4 == 0:
			print("Hasil Penjumlahannya Pasti 5 !")
			angka += 1
			print("Jumlah tebakan :", angka)
			print("Program Selesai !")
		elif angka4 == 1:
			print("Hasil Penjumlahannya Pasti 7 !")
			angka += 1
			print("Jumlah tebakan :", angka)
			print("Program Selesai !")		

if angka1 == -1: 
	tabakangka()
else: 
	print("Program tidak berhasil dijalankan")