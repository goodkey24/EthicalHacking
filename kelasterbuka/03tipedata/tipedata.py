# a = 10, a adalah variable dan 10 adalah value/nilai

#tipe data yang ada di python
#tipe data angka satuan(integer)
data_integer = 1
print("data :", data_integer)
print("-Bertipe :", type(data_integer))

#tipe data; angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("Bertipe :", type(data_integer))

#tipe data : kumpulan karakter(string)
name = "John"
print("Nama :", name)
print("tipe data :", type(name))

#tipe data : True/False (Boolean)
data_bool = True
print('data : ', data_bool)
print('bertipe :', type(data_bool))

#tipe data khusus
#bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("Bertipe :", type(data_complex))

#tipe data dari bahasa C(c_double, c_long, c_char)
from ctypes import c_double
data_c_double = c_double(10.5)
print('data :', data_c_double)
print('bertipe :', type(data_c_double))