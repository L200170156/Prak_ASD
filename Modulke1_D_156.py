print("Keterangan: jika output muncul cuma nama nomer, anda hanya perlu memanggil nama fungsi untuk memunculkan outputnya")
print ( "Nomor 1" )
def cetakSiku(x) :
    for i in range(x+1) :
        print ("*"*i)

print("Nomor 2")
def gambarlahPersegiEmpat(x,y) :
    for i in range(x) :
        if i==0 or i== x-1 :
            print ("@"*y)
        else :
            print("@" + " " * (y-2) + " @")


print("Nomor 3")
def jumlahHurufVokal(x):
    vokal="aiueoAIUEO"
    jumlah=0
    for i in x :
        if i in vokal :
            jumlah+=1
    return (len(x),jumlah)

def jumlahHurufKonsonan(x):
    vokal="aiueoAIUEO"
    jumlah=0
    for i in x :
        if i not in vokal:
            jumlah+=1
    return (len(x),jumlah)


print("Nomor 4")
def rerata(b=[]):
    x=0
    n=0
    if b!=[]:
        for i in b:
            x+=i
            n+=1
        return x/n
    return "illegal"
print(rerata([2,2]))

print("Nomor 5")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil :
        return True
    elif n in bukanprima:
        return False
    else :
        for i in range(2,int(sq(n))+1):
          if(n%i==0):
              return False
    return True

print("Nomor 6")
def cetakbilanganprima():
    prima=list()
    for i in range(2,100):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
cetakbilanganprima()


print("Nomor 7")
def faktorprima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima
print(faktorprima(143))

print("Nomor 8")
def apakahTerkandung(a,b):
    return a in b
print(apakahTerkandung("db","abcdcdsqwedb"))
print(apakahTerkandung("abd","abc"))

print("Nomor 9")
def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("pyton UMS")
            elif (i%3)==0:
                print("python")
            elif (i%5)==0:
                print("UMS")
iterasi()

print("Nomor 10")
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "determinan negatif"
    return  "determinan positif"
print(selesaikanABC(1,1,2))

print("Nomor 11")
def apakahKabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False


print("Nomor 12")
import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=str(input("Saya menyimpan sebuah angka bulat antara 1 sampai 100. coba tebak hayo. di enter ya"))
        b=int(input("masukan angka: "))
        if(b>a):
            print("terlalu besar, coba lagi")
        elif(b<a):
            print("terlalu kecil, coba lagi")
        else:
            print("benar")
            break
permainan()

print ("Nomor 13")
def katakan(a):
    angka=("","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan","sepuluh","sebelas")
    hasil=""
    n=int(a)
    if n >=0 and n<=11:
        hasil=hasil+angka[n]
    elif n<20:
        hasil=angka[(n%10)]+" belas"
    elif n<100:
        hasil=katakan(n/10)+" puluh "+katakan(n%10)
    elif n<200:
        hasil="seratus "+katakan(n-100)
    elif n<1000:
        hasil=katakan(n/100)+" ratus "+katakan(n%100)
    elif n<2000:
        hasil="seribu "+katakan(n-1000)
    elif n<1000000:
        hasil=katakan(n/1000)+" ribu "+katakan(n%1000)
    elif n<1000000000:
        hasil=katakan(n/1000000)+" juta "+katakan(n%1000000)
    return hasil


print ("Nomor 14")
def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
print(formatRupiah(30000000))





    
    
