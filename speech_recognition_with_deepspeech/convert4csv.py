#bu kodlamanın amacı,tsv dosyalarını csv dosyalarına belli kısıtlamalar ve kurallara göre düzenleyip,dönüştürmektir.
#böylece istenilen dile ait modelleme yaparken alınabilecek hataların minimuma indirilmesi amaclanmıstır.
#ASR w/Deepspeech
import os
import re
from num2words import num2words
import string

path = "/home/zoirasu/İndirilenler/tr/clips/"  # audio path belirtildi

with open("/home/zoirasu/İndirilenler/tr/invalidated.tsv", "r", encoding="utf-8") as reader:  # .tsv dosyayı okumaya açıldı
    all_lines = reader.readlines()  # tüm satırları tek tek okur.

    for i in range(len(all_lines)):  # tüm lineların uzunluğunu kadar döndür

        if i == 0:
            continue
        else:
            string_hali = all_lines[i]  # tek tek satırlari string olarak alıyor
            string_hali = string_hali.split("\t")  # tablara göre alınan stringleri bölüyor
            # print(string_hali)
            dosya_adi = string_hali[1]+".wav"  # bölünen stringin 2.elemanını dosya_adi olarak alıyor
            dosya_yolu = path + dosya_adi  # dosya yolunu dosya ismi ve pathle birleştirip asıl pathi getiriyor
            dosya_boyutu = os.path.getsize(dosya_yolu)  # dosya boyutunu bulmak için asıl path'den dosyaya erişip hesaplıyor
            cumle = string_hali[2].replace(",","").replace('"',"").translate(str.maketrans('','',string.punctuation)).lower().replace("˙","")
            # üstteki satır:bölünen stringin 3.elemanını alıyor ve cümleye atıyor.

            splitter=re.compile(r'\d+')  #sayılara göre ayır
            match1=splitter.findall(cumle) #match1 degiskenine sayıları at

            for eleman in match1: #sayılar kadar eleman degiskenine atarak döndür
             try:
                sayi=num2words(int(eleman),lang="tr") #listede dönüşebilen sayıları num2words dönüştürdü
                cumle=cumle.replace(eleman,sayi)     #cumle içinde sayilari textiyle degistirdi.
             except ValueError:   #sayi olmayanlar için ValueError alınıyordu bunun içinde hiçbir işlem yapma komutu verildi.
                pass
            print(cumle)
            satir = dosya_yolu + "," + str(dosya_boyutu) + ',' + cumle + "\n"  # her satiri oluşturuyor

            with open("/home/zoirasu/İndirilenler/tr/invalidated.csv", "a+") as writer:
                writer.write(satir.replace('"', ''))  # tırnak işareti yerine boşluk bırakıyor.
