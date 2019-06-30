
import re
import os
import time
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern
pixels.pattern = GoogleHomeLedPattern(show=pixels.show)

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("test.txt","r")
    loglines = follow(logfile)
    pattern = re.compile(r'(?<=00000\d{3,3}:)\D*')
    for line in loglines:
        print (line)
#        if re.match(r'0000*',line):
#            print('ok')
        outputtext=pattern.findall(line)
 
        if outputtext:
            if ('SAM') in outputtext[0]:
                if ('TURN ON THE LIGHT') in outputtext[0]:
                    print(outputtext[0])
                    print('ok')
                    data =[0,255,0] * 3
                    pixels.show(data)
                    os.system("sudo mpg123 turnonlight.mp3")
                                                    
  
                if ('SWITCH ON THE LIGHT') in outputtext[0]:
                    print (outputtext[0])
                    print ('ok')
                    data =[255,0,0] * 3
                    pixels.show(data)
                    os.system("sudo mpg123 turnonlight.mp3")
                else:
                    print('no')  
  
                if ('TURN OFF THE LIGHT') in outputtext[0]:      
                    print (outputtext[0])
                    print ('ko')
                    data =[0,0,0] * 3
                    pixels.show(data)
                    os.system("sudo mpg123 turnofflight.mp3")
                else:
                    print('non')
              
                if ('SWITCH OFF THE LIGHT') in outputtext[0]:
                    print (outputtext[0])
                    print ('ko')
                    data =[0,0,0] * 3
                    pixels.show(data)
                    os.system("sudo mpg123 turnofflight.mp3")
                else:
                    print('non')        
                
            
            
