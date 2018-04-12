import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import hashlib
import base64

############Edit Configuration################
email = open('timothybuske@gmail.com','staceybuske@gmail.com')
domain = "https://vacationforfree.godaddysites.com" #The Domain That You Own
company_name = "Vacations for Free" #The Company Name
me  = "auto-confirm@freevacationshome.com" + domain #Email return address
host = 'smtpout.secureserver.net' #Godaddy SMTP server
login = 'timothybuske@gmail.com' #Godaddy Login
password = 'Banjo0721??' #Godaddy password

############Edit Configuration################

for email_add in email:
    file_html = open('a.html','r')
    receiver = email_add.strip()
    print receiver + ":" + hashlib.md5(receiver.strip()).hexdigest()
    hash_email = hashlib.md5(receiver).hexdigest()
    base_email = base64.b64encode(receiver)

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'You Won a Free Vacation'
    msg['From'] = me
    msg['To'] = receiver
    msg.preamble = 'This is a multi-part message in MIME format.'


    # Create the body of the message (a plain-text and an HTML version).
    html = file_html.read()
    html = html.replace("hash_string", hash_email)
    html = html.replace("base_string", base_email)
    html = html.replace("suck.example.com", domain)
    html = html.replace("SUCK", company_name)
    file_html.close()

    # Record the MIME types of both parts - text/plain and text/html.

    part1 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part1)
    fp = open('order_details.png', 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<image1>')
    msg.attach(img)

    fp = open('cc.png', 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<cc1>')
    msg.attach(img)

    fp = open('image.jpg', 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<fire1>')
    msg.attach(img)

    fp = open('left.png', 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<left1>')
    msg.attach(img)

    fp = open('right.jpg', 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<right1>')
    msg.attach(img)

    fp = open('a.png', 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<a1>')
    msg.attach(img)


    # Send the message via local SMTP server.
    s = smtplib.SMTP_SSL(host,465)
    s.ehlo()
    s.login(login,password)
    s.sendmail(me, receiver, msg.as_string())
    s.quit()
    time.sleep(5)

