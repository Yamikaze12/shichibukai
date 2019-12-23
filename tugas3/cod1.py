def jumlah(a,b,c):
    return a+b+c
def kurang(a,b,c):
    return a-b-c
def kali(a,b,c):
    return a*b*c
def bagi(a,b,c):
    return a/b/c

    print("pilih operasi :")
    print("1.jumlah")
    print("2.kurang")
    print("3.kali")
    print("4.bagi")

choice = input("masukan pilihan 1/2/3/4 :")

angka1 = int(input("angka ke-1 : "))
angka2 = int(input("angka ke-2 : "))
angka3 = int(input("angka ke-3 : "))

if choice == '1':
    print(angka1,"+",angka2,"+",angka3,"=",jumlah(angka1,angka2,angka3))
elif choice == '2':
    print(angka1,"-",angka2,"-",angka3,"=",kurang(angka1,angka2,angka3))
elif choice == '3':
    print(angka1,"*",angka2,"*",angka3,"=",kali(angka1,angka2,angka3))
elif choice == '4':
    print(angka1,"/",angka2,"/",angka3,"=",bagi(angka1,angka2,angka3))
else:
    print("salah slur :V ")

    input('Press ENTER to exit')

    