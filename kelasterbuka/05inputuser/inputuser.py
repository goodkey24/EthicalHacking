#Mengambil input dari user

#jika tidak di casting maka input akan menghasilkan tipe data string
# data = input("Masukkan Data: ")

# print("Data : ",data, type(data))

# nama = input("Masukkan Nama : ")
# tahun = input("Tahun : ")
# alamat = input("Masukkan Alamat : ")

# print("Nama : ", str(nama))
# print("Tahun : ", int(tahun)) #harus di casting jika tidak ingin menerima input berupa string
# print("Alamat : ", str(alamat))

#spesifik untuk boolean
biner = bool(int(input("masukkan nilai boolean: ")))
print("data = ",biner, ", type = ", type(biner))