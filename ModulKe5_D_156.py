#Nomor 1
class Mahasiswa(object):
    def __init__ (self,nim) :
        self.nim = nim

a1= "L200170156"
a2= "L200170152"
a3= "L200170155"
a4= "L200170147"
a5= "L200170143"

Daftar = [a1,a2,a3,a4,a5]


print("Nomor 1")
def insertionSort(A) :
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1] :
            A[pos] = A[pos-1]
            pos = pos - 1
        A[pos] =  nilai

insertionSort(Daftar)
print("Berikut adalah NIM Mahasiswa secara urut :","\n",Daftar, "\n")


#Nomor 2
print("Nomor 2")
A = ["A100","B200","C300","D400","E500"]
B = ["F600" , "G700 " , "H700" , "I800" , "J900"]
C =[]
C.extend(A)
C.extend(B)
def insertionSort(A) :
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1] :
            A[pos] = A[pos-1]
            pos = pos - 1
        A[pos] =  nilai
insertionSort(C)
print("Nilai C yang telah urut seperti dibawah ini : ","\n",C,"\n")

#Nomor 3
print("Nomor 3")
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[q]= A[q]
    A[q]= tmp
    
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil   

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
        
k=[]
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("bubble : %g detik" %(ak-aw));
aw = detak();selectionSort(u_bub);ak=detak();print("selection: %g detik" %(ak-aw));
aw = detak();insertionSort(u_bub);ak=detak();print("insertion : %g detik" %(ak-aw));
