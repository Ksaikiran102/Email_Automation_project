#now in this case we will use email package where we can add subject to the mail and also
#we can give to address
from random import randint
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#give from adress,to adress and subject
From='kasarlasaikiran002@gmail.com'
To="22311a05n3@cse.sreenidhi.edu.in"
Subject="Email Automation"
msg=MIMEMultipart()
msg['From']=From
msg['To']=To
msg['Subject']=Subject
b=randint(1000,9999)
c=str(b)
body="Email automation Otp is"+c
msg.attach(MIMEText(body))
text=msg.as_string()
#same as previous SMTP Usage we will follow
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("kasarlasaikiran002@gmail.com","sxlk uqbw yvgm zcqe")
server.sendmail(From,To,text)
print("Success")
otp=int(input("Enter 4 digit Otp:"))
if(otp==b):
    print("Login Successfull")
else:
    print("Please Enter vaild OTP")
server.quit()
