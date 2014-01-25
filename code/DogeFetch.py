#!/usr/bin/python
# Uses a configured Adafruit_CharLCDPlate.pt
# Reference functions:

#def dogeaddress(self):
#        sleep(1)
#        dogechain = urllib2.urlopen('http://dogechain.info/chain/Dogecoin/q/addressbalance/', self)
#        balance = dogechain.read()
#        lcd.clear
#        lcd.backlight(lcd.GREEN)
#        lcd.message("BALANCE:", \n, balance)
#        
#    def dogevalue():
#        import api_parser
#        lcd.clear
#        lcd.backlight(lcd.BLUE)
#        lcd.message("VALUE:", \n, sys.argv[1])
        



from time import sleep
from CryptoCoinChartsApi import API
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

col = (('Red' , lcd.RED) , ('Yellow', lcd.YELLOW), ('Green' , lcd.GREEN),
           ('Teal', lcd.TEAL), ('Blue'  , lcd.BLUE)  , ('Violet', lcd.VIOLET),
           ('Off' , lcd.OFF) , ('On'    , lcd.ON))

    lcd = Adafruit_CharLCDPlate()
    lcd.begin(16, 2)
    lcd.clear()
    lcd.backlight(RED)
    lcd.message("Hello, I'm", \n "DogeFetch!")
    
    #lcd.message("BALANCE:", \n, balance)

    btn = ((lcd.LEFT, 'Fetching Balance', lcd.RED, lcd.addressvalue(DLLAyRd9qA6LVcJiWk2wMNjEqEVUVwbARc)),
           #(lcd.LEFT  , 'Left'  , lcd.RED),
           #(lcd.UP    , 'Up'    , lcd.BLUE),
           #(lcd.DOWN  , 'Down'  , lcd.GREEN),
           (lcd.RIGHT , 'Fetching Value' , lcd.VIOLET, lcd.dogevalue_fix))
    
    prev = -1
    while True:
        for b in btn:
            if lcd.buttonPressed(b[0]):
                if b is not prev:
                    print b[1]
                    lcd.clear()
                    lcd.message(b[1])
                    lcd.backlight(b[2])
                    # check syntax below?
                    (b[3])
                    prev = b
                break
