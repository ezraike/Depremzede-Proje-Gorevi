"""

github link: https://github.com/ezraike/Depremzede-Proje-Gorevi/blob/main/algoritma-odevguncel.py

"""

import tkinter as tk
import time
import pandas as pd
e=int(input("Selamlar, Lütfen Adminseniz 1'i Normal Kullanıcıysanız 2'yi tuşlayın:\n"))

if e==1:
    print("Admin paneline hoş geldiniz!")
    j=3
    while j>0:
        liste1=[1,2,3]
        for i in liste1:
            j-=1
            manuel_depremzede=str(input("Lütfen Kayıt Olmayan bir depremzedenin adini girin:"))
            sozluk1={"Depremzede"[i]:manuel_depremzede}
            dosya43=open("Manuel-Eklenen-Depremzedeler.txt","a")
            dosya43.write("Kullanici adi:{}  Sira Numarasi:{}\n".format(manuel_depremzede,i))
            

elif e==2:
    print("Kullanici paneline hoş geldiniz!")
    tuple1=("1.En sevdigin renk?","2.En sevdigin yemek?","3.Ilkokul Ogretmeninin adi?","4.Evcil hayvanının adı?")

    while True:
        sozluk2 = {}
        try:
            bot_kontrol = int(input(
                "Lütfen güvenlik testi icin asagida vereceğimiz sorulardan dilediğinizin numarasını tuşlayın \n {} :".format(
                    tuple1)))
        except ValueError:
            print("Lütfen tam bir sayı giriniz!")
        else:


            if bot_kontrol==1:
                soru1=input("En sevdigin renk?:")
                sozluk2["En sevdigin renk?"]=soru1
                break
            elif bot_kontrol==2:
                soru1=input("En sevdigin yemek?:")
                sozluk2["En sevdigin yemek?"]=soru1
                break
            elif bot_kontrol==3:
                soru1=input("Ilkokul Ogretmeninin adi?:")
                sozluk2["Ilkokul Ogretmeninin adi?"]=soru1
                break
            elif bot_kontrol==4:
                soru1=input("Evcil hayvanının adı?:")
                sozluk2["Evcil hayvanının adı?"]=soru1
                break
            else:
                print("Hatalı giriş yaptınız")
                print("Tekrar başlatılıyor.......")
                time.sleep(2)
                continue

    print("Sozluk oluşturuldu \n {}".format(sozluk2))
    time.sleep(3)
    print(" Bilgilendirme için Türkiye genelinde deprem felaketinden etkilenen kişi sayısını aşağıda bulabilirsiniz..")
    time.sleep(5)
    bilgi=pd.read_csv("natural-disasters2.csv",delimiter=";")

    bilgi1=bilgi.loc[1470:1479,:]
    bilgi1 = bilgi1.set_index("Year")
    print(bilgi1)


    a = int(input(
        "Lütfen yapmak istediğiniz default işlemi seçiniz: \n 1-Giriş Yap \n 2-Üye Ol \n 3- Şifremi Unuttum \n Cevabınız? :"))

    b = 0
    c = 0
    if a == 1:
        app = tk.Tk()
        app.state("normal")
        app.minsize(400, 400)
        app.maxsize(400, 400)
        app.title("Giriş Ekranına Hoş Geldiniz!")


        def giris_yap():
            dosya2 = open("Sisteme-Giren-Kullanicilar", "a")
            dosya2.write("Kullanici Adi {} , Sifre {}\n".format(kutu1.get(), kutu2.get()))
            kutu1.delete(0, "end")
            kutu2.delete(0, "end")

            app2 = tk.Tk()
            app2.state("normal")
            app2.minsize(400, 400)

            app2.title("Durumunuzu Belirtin")

            def depremzede():
                def sil2():
                    file46 = open("Hayatini_Kaybedenler.txt", "a")
                    global c
                    c += int(entry1.get())
                    file46.write("Hayatini Kaybedenlerin Sayisi {}".format(c))
                    entry1.delete(0, "end")
                    girdi46 = tk.Label(app2, text="İşleminiz Başarıyla Gerçekleştirildi, Geçmiş olsun :'(")
                    girdi46.pack()

                girdi1 = tk.Label(app2,
                                  text="Lütfen olay sırasında 1. dereceden kaç yakınınızı kaybettiğinizi sayı olarak yazın: \n",
                                  bg="white", fg="black")
                girdi1.pack()
                entry1 = tk.Entry(app2, bg="white", fg="black")
                entry1.pack()
                buton4 = tk.Button(app2, text="Onayla", bg="purple", fg="red", command=sil2)
                buton4.pack()


            def yardimsever():
                def sil1():
                    file45 = open("Yardim_Edilen_Miktar.txt", "a")
                    global b
                    b += int(entry2.get())
                    file45.write("Yapilan Bagis Miktari {}".format(b))
                    entry2.delete(0, "end")
                    entry68.delete(0,"end")
                    girdi47 = tk.Label(app2, text="Yardımlarınız için minnettarız, Tekrardan Tesekkür Ederiz ! :)")
                    girdi47.pack()

                girdi2 = tk.Label(app2, text="Yardım etmek istediğiniz miktarı sayı cinsinden yazin", bg="white",
                                  fg="black")
                girdi2.pack()
                entry2 = tk.Entry(app2, bg="white", fg="black")
                entry2.pack()
                girdi68 = tk.Label(app2, text="Not Eklemek isterseniz buraya belirtiniz:", bg="white", fg="black")
                girdi68.pack()
                entry68 = tk.Entry(app2, bg="white", fg="black")
                entry68.pack()
                buton3 = tk.Button(app2, text="Onayla", bg="purple", fg="red", command=sil1)
                buton3.pack()

            buton3 = tk.Button(app2, text="Depremzedeyim", bg="purple", fg="red", command=depremzede)
            buton3.pack()

            buton4 = tk.Button(app2, text="Yardımseverim", bg="purple", fg="red", command=yardimsever)
            buton4.pack()

            app2.mainloop()


        label1 = tk.Label(app, text="Kullanici adinizi giriniz")
        label1.place(x=70, y=70)

        kutu1 = tk.Entry(app, bg="black", fg="white")
        kutu1.place(x=200, y=70)

        label2 = tk.Label(app, text="Sifrenizi giriniz")
        label2.place(x=70, y=100)

        kutu2 = tk.Entry(app, bg="black", fg="white", show="*")
        kutu2.place(x=200, y=100)

        buton1 = tk.Button(app, text="Giris YAP", bg="white", fg="black", command=giris_yap)
        buton1.place(x=130, y=140)

        app.mainloop()

    elif a == 2:
        app = tk.Tk()
        app.state("normal")
        app.minsize(400, 400)
        app.maxsize(400, 400)
        app.title("Üye Ol Ekranına Hoş Geldiniz!")


        def giris_yap():
            dosya2 = open("Sisteme-Uye-Olan-Kullanicilar", "a")
            dosya2.write("Kullanici Adi {} , Sifre {}\n".format(kutu1.get(), kutu2.get()))
            kutu1.delete(0, "end")
            kutu2.delete(0, "end")

            app2 = tk.Tk()
            app2.state("normal")
            app2.minsize(400, 400)

            app2.title("Durumunuzu Belirtin")

            def depremzede():
                def sil2():
                    file46 = open("Hayatini_Kaybedenler.txt", "a")
                    global c
                    c += int(entry1.get())
                    file46.write("Hayatini Kaybedenlerin Sayisi {}".format(c))
                    entry1.delete(0, "end")
                    girdi46 = tk.Label(app2, text="İşleminiz Başarıyla Gerçekleştirildi, Geçmiş olsun :'(")
                    girdi46.pack()

                girdi1 = tk.Label(app2,
                                  text="Lütfen olay sırasında 1. dereceden kaç yakınınızı kaybettiğinizi sayı olarak yazın: \n",
                                  bg="white", fg="black")
                girdi1.pack()
                entry1 = tk.Entry(app2, bg="white", fg="black")
                entry1.pack()
                buton4 = tk.Button(app2, text="Onayla", bg="purple", fg="red", command=sil2)
                buton4.pack()

            def yardimsever():
                def sil1():
                    file45 = open("Yardim_Edilen_Miktar.txt", "a")
                    global b
                    b += int(entry2.get())
                    file45.write("Yapilan Bagis Miktari {}".format(b))
                    entry2.delete(0, "end")
                    entry68.delete(0, "end")
                    girdi47 = tk.Label(app2, text="Yardımlarınız için minnettarız, Tekrardan Teşekkür Ederiz ! :)")
                    girdi47.pack()

                girdi2 = tk.Label(app2, text="Yardım etmek istediğiniz miktarı sayı cinsinden yazin", bg="white",
                                  fg="black")

                girdi2.pack()
                entry2 = tk.Entry(app2, bg="white", fg="black")
                entry2.pack()
                girdi68 = tk.Label(app2, text="Not Eklemek isterseniz buraya belirtiniz:", bg="white", fg="black")
                girdi68.pack()
                entry68 = tk.Entry(app2, bg="white", fg="black")
                entry68.pack()
                buton3 = tk.Button(app2, text="Onayla", bg="purple", fg="red", command=sil1)
                buton3.pack()

            buton3 = tk.Button(app2, text="Depremzedeyim", bg="purple", fg="red", command=depremzede)
            buton3.pack()

            buton4 = tk.Button(app2, text="Yardımseverim", bg="purple", fg="red", command=yardimsever)
            buton4.pack()

            app2.mainloop()


        label1 = tk.Label(app, text="Kullanici adinizi giriniz")
        label1.place(x=70, y=70)

        kutu1 = tk.Entry(app, bg="black", fg="white")
        kutu1.place(x=200, y=70)

        label2 = tk.Label(app, text="Sifrenizi giriniz")
        label2.place(x=70, y=100)

        kutu2 = tk.Entry(app, bg="black", fg="white", show="*")
        kutu2.place(x=200, y=100)

        buton1 = tk.Button(app, text="Üye Ol", bg="white", fg="black", command=giris_yap)
        buton1.place(x=130, y=140)

        app.mainloop()
    elif a==3:
        app = tk.Tk()
        app.state("normal")
        app.minsize(400, 400)
        app.maxsize(400, 400)
        app.title("Şifremi Unuttum Ekranına Hoş Geldiniz!")


        def giris_yap():
            dosya2 = open("Sifresini_Unutan_Kullanicilar", "a")
            dosya2.write("Kullanici Adi {} , Sifre {}\n".format(kutu1.get(), kutu2.get()))
            kutu1.delete(0, "end")
            kutu2.delete(0, "end")

            app2 = tk.Tk()
            app2.state("normal")
            app2.minsize(400, 400)

            app2.title("Durumunuzu Belirtin")

            def depremzede():
                def sil2():
                    file46 = open("Hayatini_Kaybedenler.txt", "a")
                    global c
                    c += int(entry1.get())
                    file46.write("Hayatini Kaybedenlerin Sayisi {}".format(c))
                    entry1.delete(0, "end")

                    girdi46 = tk.Label(app2, text="İşleminiz Başarıyla Gerçekleştirildi, Geçmiş olsun :'(")
                    girdi46.pack()

                girdi1 = tk.Label(app2,
                                  text="Lütfen olay sırasında 1. dereceden kaç yakınınızı kaybettiğinizi sayı olarak yazın: \n",
                                  bg="white", fg="black")
                girdi1.pack()
                entry1 = tk.Entry(app2, bg="white", fg="black")
                entry1.pack()
                buton4 = tk.Button(app2, text="Onayla", bg="purple", fg="red", command=sil2)
                buton4.pack()

            def yardimsever():
                def sil1():
                    file45 = open("Yardim_Edilen_Miktar.txt", "a")
                    global b
                    b += int(entry2.get())
                    file45.write("Yapilan Bagis Miktari {}".format(b))
                    entry2.delete(0, "end")
                    entry68.delete(0, "end")
                    girdi47=tk.Label(app2,text="Yardımlarınız için minnettarız, Tekrardan Teşekkür Ederiz ! :)")
                    girdi47.pack()

                girdi2 = tk.Label(app2, text="Yardım etmek istediğiniz miktarı sayı cinsinden yazin", bg="white",
                                  fg="black")
                girdi2.pack()

                entry2 = tk.Entry(app2, bg="white", fg="black")
                entry2.pack()
                girdi68 = tk.Label(app2, text="Not Eklemek isterseniz buraya belirtiniz:", bg="white", fg="black")
                girdi68.pack()
                entry68 = tk.Entry(app2, bg="white", fg="black")
                entry68.pack()
                buton3 = tk.Button(app2, text="Onayla", bg="purple", fg="red", command=sil1)
                buton3.pack()

            buton3 = tk.Button(app2, text="Depremzedeyim", bg="purple", fg="red", command=depremzede)
            buton3.pack()

            buton4 = tk.Button(app2, text="Yardımseverim", bg="purple", fg="red", command=yardimsever)
            buton4.pack()

            app2.mainloop()


        label1 = tk.Label(app, text="Kullanici adinizi giriniz")
        label1.place(x=70, y=70)

        kutu1 = tk.Entry(app, bg="black", fg="white")
        kutu1.place(x=200, y=70)

        label2 = tk.Label(app, text="Yeni Sifrenizi giriniz")
        label2.place(x=70, y=100)

        kutu2 = tk.Entry(app, bg="black", fg="white", show="*")
        kutu2.place(x=200, y=100)

        buton1 = tk.Button(app, text="Üye Ol", bg="white", fg="black", command=giris_yap)
        buton1.place(x=130, y=140)

        app.mainloop()

    else:
        pass
