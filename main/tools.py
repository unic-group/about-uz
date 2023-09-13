import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import redirect




def contect(email ,name ):
    smtp_server = 'smtp.yandex.com'
    port = 587
    sender_email = 'about.uz@yandex.com'
    password = 'hzqgmgpulavjtpzk'
    receiver_email = email

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'ABOUT_UZ'

    body = f"Assalomu alaykum {name} . Sizga rahmat! Bizning adminlarimiz siz bilan tez orada bog'lanishadi. Biz sizning xizmatlaringiz uchun shoshilmaymiz. Agar sizning yordamingiz uchun boshqa savollar yoki talablar bo'lsa, bizning adminlarimiz sizning istaklaringizni qabul qilishadi va sizga yordam berishadi. Bizning jamoa doimiy ravishda sizga yordam berishga tayyor. Qo'llab-quvvatlash uchun sizga minnatdorman!"
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('habarmuvafaqiyatli jonatildi !')
    except Exception as e:
        print(f'habar jonatishda muammo yuz berdi: {str(e)}')
    finally:
        server.quit()
    return True