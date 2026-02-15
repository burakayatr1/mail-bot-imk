import smtplib
import os
import time
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from email.utils import formatdate, make_msgid

gonderen_mail = "burakkaya.imk@gmail.com"
uygulama_sifresi = os.getenv("SIFRE") 
konu = "İTÜ İMK | Networking Time Etkinliği hk."
dosya_yolu = r"C:\Users\ASUS\Downloads\NT_sunum.pdf"
logo_yolu = r"C:\Users\ASUS\Downloads\imklogo.png"

kullanicilar = {
    "burcu.bag@hepsiburada.com": ["Burcu", "Hanım"],
    "naz.yilmaz@hepsiburada.com": ["Naz", "Hanım"],
    "sevval.koyuncuoglu@hepsiburada.com": ["Şevval", "Hanım"],
    "senay.gumusoglu@hepsiburada.com": ["Senay", "Hanım"],
    "ayca.ilindir@hepsiburada.com": ["Ayça", "Hanım"],
    "gizem.cetin@hepsiburada.com": ["Gizem", "Hanım"],
    "ozge.genc@hepsiburada.com": ["Özge", "Hanım"],
    "buket.ugur@yildizholding.com.tr": ["Buket", "Hanım"],
    "gokce.korkmaz@yildizholding.com.tr": ["Gökçe", "Hanım"],
    "busra.catir@yildizholding.com.tr": ["Büşra", "Hanım"],
    "eslem.demirel@yildizholding.com.tr": ["Eslem", "Hanım"],
    "nida.karakoc@yildizholding.com.tr": ["Nida", "Hanım"],
}

html_icerik = """
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <p>Merhaba {isim} {hitap},</p>
    
    <p>Ben, İstanbul Teknik Üniversitesi İşletme Mühendisliği Kulübü üyesi ve Networking Time Koordinatörü <b>Burak Kaya</b>. 
    Sizlerle, 2 Nisan 2026 tarihinde hibrit olarak düzenlenecek 27. Yönetim Bilimleri Kongresi kapsamında gerçekleştireceğimiz 
    <b>Networking Time</b> organizasyonu için iletişime geçiyorum.</p>

    <p>İTÜ İşletme Mühendisliği Kulübü olarak 1991 yılından bu yana iş dünyası ile öğrenciler arasında güçlü bağlar kurmayı hedefleyen birçok prestijli etkinlik düzenlemekteyiz. Bu doğrultuda her yıl gerçekleştirilen Yönetim Bilimleri Kongresi, akademi ve iş dünyasını bir araya getiren köklü bir organizasyondur. Geçtiğimiz yıl hibrit formatta düzenlenen kongre; 30’dan fazla konuşmacı, 25’in üzerinde oturum, 2.500’ü aşkın yüz yüze katılımcı ve 10.000’den fazla çevrimiçi izleyiciyi ağırlamıştır. Trendyol, Microsoft, Samsung ve Sabancı Holding gibi sektörün önde gelen kurumlarından yöneticilerin yer aldığı bu yapı, kongrenin ve alt etkinliklerinin kurumsal niteliğini ortaya koymaktadır.</p>

    <p>Bu kapsamda düzenlenen Networking Time, özellikle 3. ve 4. sınıf üniversite öğrencilerini, kariyer hedefleri doğrultusunda ilerlemek istedikleri sektörlerin temsilcileriyle birebir görüşmeler aracılığıyla bir araya getirmeyi amaçlayan özel bir networking etkinliğidir. Yapay zekâ destekli eşleştirme sistemimiz sayesinde şirketlerin ihtiyaç ve beklentilerine uygun adaylarla doğrudan ve verimli bir şekilde buluşmaları hedeflenmektedir.</p>

    <p>Sektördeki güçlü konumunuz doğrultusunda, sizleri Networking Time’da aramızda görmekten büyük memnuniyet duyarız. Etkinliğin işleyiş süreci, başvuru koşulları ve olası iş birliği olanaklarını sizinle kısa bir toplantı çerçevesinde detaylı olarak paylaşmak isteriz. Etkinliğe ilişkin ayrıntılı bilgilerin yer aldığı sunumu incelemeniz için mail ekinde paylaşıyoruz.</p>

    <p>Sizlerle iletişime geçerek etkinlik sürecini detaylandırmayı dört gözle bekliyoruz. Her türlü sorunuz için benimle ya da aşağıda iletişim bilgileri yer alan etkinlik koordinatörlerimizle iletişime geçebilirsiniz.</p>

    <p><b>Etkinlik Koordinatörleri:</b><br>
    Melis Dinçer – melisdincer.imk@gmail.com | 0541 380 60 22<br>
    Burak Kaya – burakkaya.imk@gmail.com | 0542 687 53 93</p>

    <p>İlginiz ve katkılarınız için şimdiden teşekkür eder, geri dönüşünüzü sabırsızlıkla bekleriz.</p>
    
    <p>Saygılarımla,</p>

    <br>
    <table cellpadding="0" cellspacing="0" style="font-family: Arial, sans-serif; border-collapse: collapse;">
      <tr>
        <td style="padding-right: 20px; text-align: center; vertical-align: middle;">
          <img src="cid:logo_resmi" alt="İTÜ İMK" width="130" style="display: block; margin-bottom: 10px;">
          <div style="margin-top: 10px;">
            <a href="https://www.linkedin.com/company/ituimk/"><img src="https://cdn-icons-png.flaticon.com/32/174/174857.png" width="18"></a>
            <a href="https://www.instagram.com/ituimk/"><img src="https://cdn-icons-png.flaticon.com/32/2111/2111463.png" width="18"></a>
          </div>
        </td>
        <td style="border-left: 2px solid #003366; height: 110px;"></td>
        <td style="padding-left: 20px; vertical-align: middle;">
          <div style="font-size: 19px; font-weight: bold; color: #003366;">Burak Kaya</div>
          <div style="font-size: 14px; color: #555;">Networking Time Koordinatörü</div>
          <div style="font-size: 13px; margin-top: 5px;"><b style="color: #003366;">m:</b> 0542 687 53 93</div>
          <div style="font-size: 13px;"><b style="color: #003366;">e:</b> burakkaya.imk@gmail.com</div>
          <div style="font-size: 14px; font-weight: bold; color: #003366; margin-top: 5px;">İTÜ İşletme Mühendisliği Kulübü</div>
          <a href="https://www.linkedin.com/in/burak-kaya-11b6a9227/"><img src="https://cdn-icons-png.flaticon.com/32/174/174857.png" width="22" style="margin-top:8px;"></a>
        </td>
      </tr>
    </table>
  </body>
</html>
"""

def mail_gonder():
    server = None
    count = 0
    
    try:
        if not uygulama_sifresi:
            print("Hata: SIFRE bulunamadı!")
            return

        # Bağlantıyı başlat
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gonderen_mail, uygulama_sifresi)

        for mail, bilgiler in kullanicilar.items():
            isim, hitap = bilgiler[0], bilgiler[1]
            
            # --- MAIL YAPISI ---
            msg = MIMEMultipart('mixed')
            msg['From'] = f"Burak Kaya | İTÜ İMK <{gonderen_mail}>"
            msg['To'] = mail
            msg['Subject'] = konu
            msg['Date'] = formatdate(localtime=True)
            msg['Message-ID'] = make_msgid()

            msg_body = MIMEMultipart('related')
            msg.attach(msg_body)
            msg_alt = MIMEMultipart('alternative')
            msg_body.attach(msg_alt)
            msg_alt.attach(MIMEText(html_icerik.format(isim=isim, hitap=hitap), 'html'))

            # Logo Ekleme
            if os.path.exists(logo_yolu):
                with open(logo_yolu, 'rb') as f:
                    img = MIMEImage(f.read())
                    img.add_header('Content-ID', '<logo_resmi>')
                    msg_body.attach(img)

            # PDF Ekleme
            if os.path.exists(dosya_yolu):
                with open(dosya_yolu, "rb") as ek:
                    part = MIMEBase('application', 'pdf')
                    part.set_payload(ek.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(dosya_yolu)}"')
                    msg.attach(part)

            # --- GÖNDERİM ---
            server.send_message(msg)
            count += 1
            print(f"[{count}] Gönderildi: {isim} ({mail})")

            # --- GÜVENLİK BEKLEMELERİ ---
            if count < len(kullanicilar):
                # Her mail arası 20-40 saniye rastgele bekle (Çok kritik!)
                bekleme = random.randint(20, 40)
                print(f"Güvenlik uykusu: {bekleme} saniye...")
                time.sleep(bekleme)

            # Her 15 mailde bir bağlantıyı tazele (Hesabı dinlendirir)
            if count % 7 == 0 and count < len(kullanicilar):
                print("\n--- Google Dinlendirme Molası (2 Dakika) ---")
                server.quit()
                time.sleep(120)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(gonderen_mail, uygulama_sifresi)

    except Exception as e:
        print(f"\nBİR HATA OLUŞTU, DURDURULDU: {e}")
    finally:
        if server:
            server.quit()
            print("\nBağlantı güvenli şekilde kapatıldı.")

if __name__ == "__main__":
    mail_gonder()