#casting tipe data ke tipe data lainnya

#CASTING DATA INTEGER
print("====CASTING TIPE DATA INTEGER====")
data_int = 9
print('data =', data_int,", tipe data:", type(data_int))
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # nilai akan menjadi false jika value dari data_int = 0
print('data : ', data_float, ", bertipe :", type(data_float))
print('data : ', data_str, ", bertipe :", type(data_str))
print('data : ', data_bool, ", bertipe :", type(data_bool))

#CASTING DATA FLOAT
print("====CASTING TIPE DATA FLOAT=======")
data_float = 9.5
data_int = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float) # nilai akan menjadi false jika value dari data_float = 0
print('data : ', data_int, ", bertipe :", type(data_int))
print('data : ', data_str, ", bertipe :", type(data_str))
print('data : ', data_bool, ", bertipe :", type(data_bool))

#CASTING TIPE DATA BOOL
print("====CASTING TIPE DATA BOOOL=======")
data_bool = True
data_int = int(data_bool)
data_str   = str(data_bool)
data_float  = float(data_bool) 
print('data : ', data_int, ", bertipe :", type(data_int))
print('data : ', data_str, ", bertipe :", type(data_str))
print('data : ', data_float, ", bertipe :", type(data_float))

#CASTING TIPE DATA STRING
print("====CASTING TIPE DATA STRING=======")
data_str = "100" # String harus angka
data_int = int(data_str) # jika ingin casting dari string ke int maka value stringnya  harus angka
data_bool   = bool(data_str)
data_float  = float(data_str) 
print('data : ', data_int, ", bertipe :", type(data_int))
print('data : ', data_bool, ", bertipe :", type(data_bool))
print('data : ', data_float, ", bertipe :", type(data_float))