import smtplib

from email.header import Header
from email.mime.text import MIMEText

def _get_text_charset():
    return "UTF-8"

def _get_address_charset():
    return "us-ascii"

def get_Header(name, address):
    header = Header(name, _get_text_charset())
    header.append("<{}>".format(address), _get_address_charset())
    return header


msg = MIMEText("Тестовое письмо", "plain", _get_text_charset())
msg["Subject"] = Header("Уведомление", _get_text_charset())
# h = Header("Николай", text_charset)
# h.append("<nikoay_dvn@ramler.ru>", "us-ascii")
msg["From"] = get_Header("Николай", "nikoay_dvn@ramler.ru")
# h = Header("Николай Беспалов", text_charset)
# h.append("<bespalov@diasoft-service.ru>", )
# msg["To"] = get_Header("Николай Беспалов", "bespalov@diasoft-service.ru")
msg["To"] = (get_Header("Николай", "privod.org@gmail.ru"))

print(msg)

smtp = smtplib.SMTP("mail.rambler.ru", 587)
smtp.set_debuglevel(1)
smtp.starttls()
smtp.login("nikolay_dvn@rambler.ru", "Ktqnf5Rjhatjl")
smtp.sendmail(msg["From"], msg["To"], msg.as_string())
smtp.quit()
