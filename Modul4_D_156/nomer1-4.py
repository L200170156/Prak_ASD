class mhsTIF():
    def __init__(self, nama, asal, saku):
        self.nama = nama
        self.asal = asal
        self.saku = saku

c0 = mhsTIF('Muhibah','Kuala Tungkal',50000)
c1 = mhsTIF('Nindi','klaten', 60000)
c2 = mhsTIF('Yarin','salatiga',80000)
c3 = mhsTIF('Corry','klaten',70000)
c4 = mhsTIF('Ayasha','surakarta',90000)
c5 = mhsTIF('Aini','salatiga',60000)
c6 = mhsTIF('Sayangku','sukoharjo',30000)

daftar = [c0,c1,c2,c3,c4,c5,c6]

#Nomer 1
def cari(n):
    baru = []
    for i in range(len(n)):
        if(n[i].asal.lower() == 'klaten'):
            baru.append(i)
    return baru

#Nomer 2
def sakuKcl(n):
    baru = n[0].saku
    for i in range(len(n)):
        if(n[i].saku<baru):
            baru = n[i].saku
    return baru

#Nomer 3
def sakuKcl2(n):
    baru = n[0].saku
    list = []
    for i in range(len(n)):
        if(n[i].saku==baru):
            list.append(n[i].nama)
        elif(n[i].saku<baru):
            baru = n[i].saku
            list = []
            list.append(n[i].nama)
    return list

#Nomer 4
def sakuKrg(n):
    batas = 250000
    list = []
    for i in range(len(n)):
        if(n[i].saku < batas):
            list.append(n[i].nama)
    return list


print(cari(daftar))
print(sakuKcl(daftar))
print(sakuKcl2(daftar))
print(sakuKrg(daftar))
