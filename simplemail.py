'''
Step 1:-->Setting up Gmail App Password(2 step verification)
#sxlk uqbw yvgm zcqe
We will use SMTP (simple Mail Transfer Protocol)
Step 2:using SMTPLIB we start the communication

'''
import smtplib
#first we will make the protocol connection
From=input("Enter mail Address:")
To=input('Enter To Email address:')
pas=input("Enter 12 letter password")
server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
#Start Communication
server.starttls()
#we will make the login
server.login(From,pas)
print("Login Success")
messsage="Hello,This is an Automated Mail"
#send the mail
server.sendmail(From,To,messsage)
print("Success")
