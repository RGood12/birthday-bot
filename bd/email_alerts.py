import smtplib
from email.mime.text import MIMEText
from bd.secrets import recipient_email, recipient_mobile, APP_PASSWORD

sender = "randylinuxserver@gmail.com"
recipients = [recipient_mobile]
password = APP_PASSWORD


def send_error_alert(*args):

    msg = MIMEText(f"\n\nThere was an error sending {args[0]}'s birthday message: {args[1]}")
    msg['Subject'] = " ERROR! Birthday Bot"
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())

def send_nophoto_alert(*args):
    
    msg = MIMEText(f"\n\nWarning: {args[0]}'s birthday is in {args[1]} days but there are no photos available in Google Drive")
    msg['Subject'] = " WARNING! Missing Buddy Photo"
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())

