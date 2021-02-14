#!/usr/bin/env python3
# Bir ürünün fiyatının düştüğünde istenilen mail'e bilgilendirme yapan script.
import requests
from bs4 import BeautifulSoup
import smtplib
import time

#takip edilecek ürün/site url'si
URL =' burada ürün urlsi olacak.'
indirimli_fiyat = 1.500 #fiyat yaz.
#Tarayıcı bilgilerim.
headers = {'User-Agent':'Kullanıcı sistem bilgileri '}

def kontrol_Et(URL,headers,indirimli_fiyat):
    #request istegi atılır
    page = requests.get(URL,headers=headers)

    #request sonucunda elde edilen html içeriğini dönüştür.
    soup = BeautifulSoup(page.content,'html.parser')

    urun = soup.find(id="product-name").get_text().strip()  #urun ismini al
    fiyat = soup.find(id="offering-price").get_text().strip() #fiyatı al
    fiyat_ = float(fiyat[:5]) # string'i float olarak dönüştür.
    print(urun)
    print(fiyat_)
    if(fiyat_< indirimli_fiyat):
       mail_At()
def mail_At():
    frm = "umtsrz.7474@gmail.com"
    to = "umitsariozz@gmail.com"
    psw ="google uygulama parolası / google apps psw"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(frm,psw)
    subject = "Fiyat Düştü !"
    body = "Linki kontrol et : ürünün url'si "
    msg = f"Subject: {subject} \n{body}"
    msg = msg.encode('utf-8')

    server.sendmail(frm,to,msg)
    print("Aksiyon tespit edildi --> E-mail Gönderildi!!!")
    server.quit()
if __name__ == '__main__':
    while True:
        kontrol_Et(URL, headers, indirimli_fiyat)
        time.sleep(60 * 60 * 4)


