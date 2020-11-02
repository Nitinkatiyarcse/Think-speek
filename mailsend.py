import smtplib

smtpuser = "ritesh9011988@gmail.com"
smtppass = "r0h@n0990"

toadd = "ritesh9011988@gmail.com"
fromadd = smtpuser

subject = "Python Test"
header = "To: "+toadd+'\n'+"From: "+fromadd+'\n'+"Subject: "+subject+'\n'
body = "Python Script"

message = header+'\n'+body

print(message)

s = smtplib.SMTP("smtp.gmail.com",587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpuser, smtppass)
s.sendmail(fromadd, toadd, message)

s.quit()


