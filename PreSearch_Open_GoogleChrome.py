#There are some changes you should do with your code after installing python on your PC.

import time
import random
import os
import webbrowser


tokenCount = int(input("token count : "))
repeatTime = int(input("sleep time : "))

for z in range(1, tokenCount + 1):
    url = f'https://engine.presearch.org/search?q=num{random.randint(1,100)}ber+{random.randint(1,1000)}'

    webbrowser.register('chrome',
    	None,

        #You should find out your chrome.exe location on your computer and paste it down here.
    	webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
        
    webbrowser.get('chrome').open(url)
    
    time.sleep(repeatTime)
    print (z)  

    if z%10 == 0:
        while 1 :
            os.system("TASKKILL /F /IM chrome.exe")
            time.sleep(6)
            break