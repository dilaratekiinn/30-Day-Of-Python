import sqlite3
con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,Yazar TEXT, Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplık Values ('İstanbul Hatırası','Ahmet Ümit ', 'Everest ', 561 )")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute ("Insert into kitaplık Values (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste= cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al2 ():
    cursor.execute("Select isim,Yazar From kitaplık")
    liste= cursor.fetchall()
    print ("Kitaplık tablosunun bilgileri..")
    for i in liste:
        print(i)
def verileri_al3(Yayınevi):
   cursor.execute("Select * From  kitaplık where Yayınevi = ?" ,(Yayınevi,))
   liste = cursor.fetchall()
   print ("Kitaplık tablasonun bilgileri....")
   for i in liste:
       print(i)


def verileriguncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ? ",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def verilerisil(Yazar):
 cursor.execute("Delete From kitaplık where Yazar = ?", (Yazar,))
 con.commit()
 
verileri_al()
con.close()
