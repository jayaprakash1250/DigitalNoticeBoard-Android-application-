#import Libraries
import RPi.GPIO as GPIO
import time
from pyrebase import pyrebase
import LiquidCrystalPi


#Firebase Configuration
# (*) Should be changed by your own data
config = {
   "apiKey": "AIzaSyACRUoCQQ9TQSCblg8NahYOrQH-CjK1Ycs",
    "authDomain":"digitalnoticeboardproject.firebaseapp.com",
    "databaseURL": "https://digitalnoticeboardproject.firebaseio.com",
    "projectId": "digitalnoticeboardproject",
    "storageBucket": "digitalnoticeboardproject.appspot.com",
    "messagingSenderId": "200473268318"
    }

firebase = pyrebase.initialize_app(config)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LCD = LiquidCrystalPi.LCD(29, 31, 33, 35, 37, 38)

LCD.begin(16,2)

time.sleep(0.5)
LCD.write("      VVIT     ")

LCD.nextline()

time.sleep(0.5)
LCD.write(" D-Notice Board")
#Firebase Database Intialization
db = firebase.database()

#While loop to run until user kills program
while(True):
    notice = db.child("Notice").get()
    str = notice.val()
    if(len(str)==0):
        LCD.clear()
        LCD.write("      VVIT     ")
        LCD.nextline()
        LCD.write(" D-Notice Board")
    elif(len(str)<=16):
        LCD.clear()
        LCD.write(str)
    else:
        str1 ="".join(str[:16])
        str2 ="".join(str[16:])
        LCD.clear()
        LCD.write(str1)
        LCD.nextline()
        LCD.write(str2)
