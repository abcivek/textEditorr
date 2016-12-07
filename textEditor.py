kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"
çeviri_tablosu = str.maketrans(kaynak, hedef)
metin=input("Lütfen düzenlemek istediğiniz metni giriniz: ")
metin2=metin

while True:
    
    if not metin:
        print("Bu bölüm boş bırakılamaz!")
        metin=input("Lütfen düzenlemek istediğiniz metni giriniz: ")
        
        
    secenek=input("""\nYapmak istediğiniz işlem numarasını belirtiniz

    Seçenekler:\n
    1-Karakter/kelime değiştir
    2-Tüm harfleri küçült
    3-Tüm harfleri büyüt
    4-Metnin ilk harfini büyüt
    5-Her kelimenin ilk harfini büyüt
    6-Gereksiz karakterleri temizle
    7-Belli bir karakterin kaç kez geçtiğini sorgula
    8-Karakterin yerini bul
    9-Metni ortala
    10-Metni hizala
    11-Encoding'i değiştir
    12-Sekme boşluklarını genişlet
    13-Metni Türkçe karakterlerden arındır
    14-Tüm işlemleri geri al
    15-Metni ekrana bastır
    16-Çık

    İşlem numarası: """)
   
    if not secenek:
        print("Bu bölüm boş bırakılamaz!! Lürfen bir seçenek seçiniz...")
    if secenek=="16":
        print("Çıkılıyor...")
        exit()
    elif secenek=="1":
        eski=input("Degiştirmek istediğiniz karakter nedir: ")
        if eski not in metin:
            print("Bu karakter metninizde geçmiyor!")
            print(eski)
        else:
            yeni=input("Onu ne ile değiştirmek istiyorsunuz?: ")
            metin=metin.replace(eski,yeni)
        print(metin)
        
    elif secenek=="2":
        metin=metin.lower()
        print(metin)
    elif secenek=="3":
        metin=metin.upper()
        print(metin)
    elif secenek=="4":
        metin=metin.capitalize()
        print(metin)
    elif secenek=="5":
        metin=metin.title()
        print(metin)
    elif secenek=="6":
        gereksiz=input("Temizlemek istediğiniz karakteri giriniz: ")
        soru=input("Bu karakter soldan, sağdan mı yoksa her iki taraftan mı temizlensin? l/r/b")
        gereks=input("Gereksiz boşluklar da temizlensin mi?: e/h")
        if gereks=="e":
            metin=metin.strip()
        elif gereks=="h":
            print("Boşluklar bırakılıyor...")
        else:
            print("Geçersiz bir karakter girdiniz.")
        if soru=="l":
            metin=metin.lstrip(gereksiz)
        if soru=="r":
            metin=metin.rstrip(gereksiz)
        if soru=="b":
            metin=metin.strip(gereksiz)
        else:
            print("Geçersiz bir karakter girdiniz...")
        print(metin)
        
    elif secenek=="7":
        kackez=input("Hangi karakter için sorgu yapacaksınız?")
        kac=metin.count(kackez)
        print(kackez, "karakteri metninizde",kac,"kez geçiyor")
    elif secenek=="8":
        yer=input("Yerini bulmak istediğiniz karakter: ")
        sıra=metin.index(yer)
        print("karakteriniz",sıra,". sırada")
    elif secenek=="9":
        merkez=int(input("Ortalama genişliği: "))
        ekstra=input("Kenarlara eklemek istediğiniz ekstra karakter var mı? e/h ")
        if ekstra=="e":
            ne=input("Ekstra karakter nedir?: ")
            metin=metin.center(merkez,ne)
        elif ekstra=="h":
            metin=metin.center(merkez)
        else:
            print("Geçersiz bir karakter girdiniz")
        print (metin)
    elif secenek=="10":
        yasla=input("Metni sağa mı sola mı yaslayalım? l/r: ")
        birim=int(input("Kaç birim yaslayalım? "))
        if yasla=="l":
            metin=metin.ljust(birim)
        elif yasla=="r":
            metin=metin.rjust(birim)
        else:
            print("Geçersiz bir karakter girdiniz...")
        print(metin)
    elif secenek=="11":
        kodlama=input("Metninizde istediğiniz kodlamayı yazın: ")
        metin=metin.encode(kodlama)
        print(metin)
    elif secenek=="12":
        genis=int(input("Sekme boşlukları ne kadar genişlesin? "))
        metin=metin.expandtabs(genis)
        print(metin)
    elif secenek=="13":
        print(metin.translate(çeviri_tablosu))
    elif secenek=="14":
        metin=metin2
        print(metin)
    elif secenek=="15":
        print(metin)

