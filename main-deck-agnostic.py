import pyautogui as pg
import numpy as np
from AppOpener import open
import time

def findImageThenClick(img_name, ConfidLvL=.8, MouseSpeedTime=.05, Move=True):
    a = pg.locateCenterOnScreen(img_name, confidence=ConfidLvL)
    pg.moveTo(a[0],a[1], MouseSpeedTime)
    pg.click()

print(": )")
time.sleep(5)
try :
    findImageThenClick(r'images/MinimizeCMD.png')
except :
    pass

try:
    open("Google Play Games Beta") 
    time.sleep(5)
    googlepg = pg.getWindowsWithTitle('Google Play Games Beta')[0]
    googlepg.maximize()
except : pass

time.sleep(10)


try :
    findImageThenClick(r'images/Library.png')
    time.sleep(5)
    findImageThenClick(r'images/Start.png')
    
    time.sleep(20)

except : pass


clash_royale = pg.getWindowsWithTitle('Clash Royale')[0]
clash_royale.maximize()
clash_royale.moveTo(1200,1)

time.sleep(15)

#Game loop 
while True:
    a = pg.locateCenterOnScreen(r'images/BattleButton.png', confidence=0.6)
    ok = pg.locateCenterOnScreen(r'images/OkButton.png', confidence=0.9)
    # p = pg.locateCenterOnScreen(r'images/Pekka.png', confidence=0.9,region=(1315,833,1745,995))
    # mk = pg.locateCenterOnScreen(r'images/MegaKnight.png',confidence=0.9,region=(1315,833,1745,995))
    # hr = pg.locateCenterOnScreen(r'images/HogRider.png',confidence=0.9,region=(1315,833,1745,995))
    # gg = pg.locateCenterOnScreen(r'images/GoblinGiant.png',confidence=0.9,region=(1315,833,1745,995))
    # mw = pg.locateCenterOnScreen(r'images/MotherWitch.png',confidence=0.9,region=(1315,833,1745,995))
    # mh = pg.locateCenterOnScreen(r'images/MinionHorde.png',confidence=0.9,region=(1315,833,1745,995))
    # rg = pg.locateCenterOnScreen(r'images/RoyalGiant.png',confidence=0.9,region=(1315,833,1745,995))
    # eg = pg.locateCenterOnScreen(r'images/ElectroGiant.png',confidence=0.9,region=(1315,833,1745,995))
    if a != None: 
        print("NOT IN BATTLE!!")
        pg.moveTo(a[0],a[1], 0.04)
        pg.click()
        time.sleep(10)
        
    elif ok != None : 
        print("ENDING BATTLE!!")
        pg.moveTo(ok[0],ok[1], 0.04)
        pg.click()
        time.sleep(10)
    else:
        print('IN BATTLE !!!!!')
        random_pixel_x = np.random.randint(1315,1745)
        random_pixel_y = np.random.randint(833,995)
        px = pg.pixel(random_pixel_x, random_pixel_y)
        
        print(px)
        print(random_pixel_x,random_pixel_y)
        # if px[0] < 132 and px[1] < 132 and px[2] < 132 and px[0] < 128 and px[1] < 128 and px[2] < 128:  

        pg.moveTo(random_pixel_x,random_pixel_y,0.05)
        pg.click()
        pg.moveTo(np.random.randint(1266,1707),np.random.randint(685,767),0.05)
        pg.click()

        time.sleep(1)
    # time.sleep(1)