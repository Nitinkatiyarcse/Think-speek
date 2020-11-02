import smtplib
import time
import glob
import os
os.chdir('/home/pi/Raspberry Programs/lcd')
import lcdheader as lcd
lcd.lcd_init()
GPIO.setup(3,GPIO.IN)
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
file_folder = device_folder + '/w1_slave'
print("welcome to Tempreature Sensor")

smtpuser = "yourmailid@gmail.com"
smtppass = "yourpassword"

toadd = "sendermailid"
fromadd = smtpuser
subject = "Temperature Value"
header = "To: "+toadd+'\n'+"From: "+fromadd+'\n'+"Subject: "+subject+'\n'
while True:
        print("The temperature inside room is = ")
        first=open(file_folder,"r")
        data1=first.read()
        first.close()
        (discard,sep,reading1)=data1.partition('t=')
        temp1=float(reading1)/1000
        ans=str(temp1)+"*C"
        print(ans)
        lcd.lcd_gotoxy(0,0)
        lcd.lcd_string("Temperature :-")
        lcd.lcd_gotoxy(0,1)
        lcd.lcd_string(ans)
			while GPIO.input(3):
				body = "Temperature is - "+ans
				message = header+'\n'+body
				print(message)
				s = smtplib.SMTP("smtp.gmail.com",587)
				s.ehlo()
				s.starttls()
				s.ehlo()
				s.login(smtpuser, smtppass)
				s.sendmail(fromadd, toadd, message)
				s.quit()
        time.sleep(2)