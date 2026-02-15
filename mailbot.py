import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import os

print("commit için deneme")


gonderen_mail = "burakkaya.imk@gmail.com"  # gönderen mail
uygulama_sifresi = os.getenv("SIFRE")  # 16 haneli uygulama şifresi
konu = "İTÜ İMK | Networking Time Etkinliği hk."  # hakkında kısmı
dosya_yolu = r"C:\Users\ASUS\Downloads\NT_sunum.pdf"  # sunum dosyası
logo_yolu = r"C:\Users\ASUS\Downloads\logo.png"  # imza logo
linkedin_link = "https://www.linkedin.com/in/user_name/"  # linkedin link
title = "Networking Time Koordinatörü"  # title

kullanicilar = {
    "melisdincer.imk@gmail.com": ["Melis", "Hanım"],
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
          <div style="font-size: 14px; color: #555;">{title}</div>
          <div style="font-size: 13px; margin-top: 5px;"><b style="color: #003366;">m:</b> 0542 687 53 93</div>
          <div style="font-size: 13px;"><b style="color: #003366;">e:</b> {gonderen_mail}</div>
          <div style="font-size: 14px; font-weight: bold; color: #003366; margin-top: 5px;">İTÜ İşletme Mühendisliği Kulübü</div>
          <a href={linkedin_link}><img src="https://cdn-icons-png.flaticon.com/32/174/174857.png" width="22" style="margin-top:8px;"></a>
        </td>
      </tr>
    </table>
  </body>
</html>
"""


def mail_gonder():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gonderen_mail, uygulama_sifresi)

        for mail, bilgiler in kullanicilar.items():
            isim, hitap = bilgiler[0], bilgiler[1]
            msg = MIMEMultipart("related")
            msg["From"] = gonderen_mail
            msg["To"] = mail
            msg["Subject"] = konu

            msg_alternative = MIMEMultipart("alternative")
            msg.attach(msg_alternative)
            msg_alternative.attach(
                MIMEText(html_icerik.format(isim=isim, hitap=hitap), "html")
            )

            if os.path.exists(logo_yolu):
                with open(logo_yolu, "rb") as f:
                    img = MIMEImage(f.read())
                    img.add_header("Content-ID", "<logo_resmi>")
                    msg.attach(img)

            if os.path.exists(dosya_yolu):
                with open(dosya_yolu, "rb") as ek:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(ek.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={os.path.basename(dosya_yolu)}",
                    )
                    msg.attach(part)

            server.send_message(msg)
            print(f"Gönderildi: {isim}")

        server.quit()
        print("İşlem tamam!")
    except Exception as e:
        print(f"Hata: {e}")


if __name__ == "__main__":
    mail_gonder()
