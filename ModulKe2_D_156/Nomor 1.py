class Pesan(object):
    """Sebuah kelas pertama pesan.
    untuk memahami konsep class dan object"""
    def __init__(self,sebuahString):
        self.teks= sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks),'karakter.')
    def perbarui(self,stringbaru):
        self.teks = stringbaru

    #1a
    def apakahTerkandung(self,string):
        return string in self.teks

    #1b
    def hitungKonsonan(self):
        jumlah = 0
        vokal = "aiueoAIUEO"
        for x in self.teks:
            if x not in vokal:
                jumlah += 1
        return jumlah

    #1c
    def hitungVokal(self):
        jumlah = 0
        vokal = "aiueoAIUEO"
        for x in self.teks:
            if x in vokal:
                jumlah += 1
        return jumlah
