import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


adres_smtp = "smtp.gmail.com"  
port_smtp = 587  
uzytkownik_smtp = "employeepage595@gmail.com"
haslo_smtp = "TestoweHaslo123-"

wiadomosc = MIMEMultipart()
wiadomosc["From"] = uzytkownik_smtp
wiadomosc["To"] = "zuza.m.makowska@gmail.com"
wiadomosc["Subject"] = "Sample Title"

tresc = "Sample content"
wiadomosc.attach(MIMEText(tresc, "plain"))

try:
    serwer = smtplib.SMTP(adres_smtp, port_smtp)
    serwer.starttls()  
    serwer.login(uzytkownik_smtp, haslo_smtp)
    serwer.send_message(wiadomosc)
    serwer.quit()
    print("Message sent")
except Exception as e:
    print(f"Error ocurred while sending the message: {e}")
