import pyautogui as pg
import numpy as np
from AppOpener import open
import time

def findImageThenClick(img_name, ConfidLvL=.8, MouseSpeedTime=.05, Move=True):
    a = pg.locateCenterOnScreen(img_name, confidence=ConfidLvL)
    pg.moveTo(a[0],a[1], MouseSpeedTime)
    pg.click()

findImageThenClick(r'images/MinimizeCMD.png')

open("Google Play Games Beta") 
time.sleep(5)
googlepg = pg.getWindowsWithTitle('Google Play Games Beta')[0]
googlepg.maximize()

time.sleep(10)



findImageThenClick(r'images/Library.png')
time.sleep(5)
findImageThenClick(r'images/Start.png')

time.sleep(20)

clash_royale = pg.getWindowsWithTitle('Clash Royale')[0]
clash_royale.maximize()
clash_royale.moveTo(1200,1)

time.sleep(30)

#Game loop 
while True:
    a = pg.locateCenterOnScreen(r'images/BattleButton.png', confidence=0.9)
    ok = pg.locateCenterOnScreen(r'images/OkButton.png', confidence=0.9)
    p = pg.locateCenterOnScreen(r'images/Pekka.png', confidence=0.9,region=(1315,833,1745,995))
    mk = pg.locateCenterOnScreen(r'images/MegaKnight.png',confidence=0.9,region=(1315,833,1745,995))
    hr = pg.locateCenterOnScreen(r'images/HogRider.png',confidence=0.9,region=(1315,833,1745,995))
    gg = pg.locateCenterOnScreen(r'images/GoblinGiant.png',confidence=0.9,region=(1315,833,1745,995))
    mw = pg.locateCenterOnScreen(r'images/MotherWitch.png',confidence=0.9,region=(1315,833,1745,995))
    mh = pg.locateCenterOnScreen(r'images/MinionHorde.png',confidence=0.9,region=(1315,833,1745,995))
    rg = pg.locateCenterOnScreen(r'images/RoyalGiant.png',confidence=0.9,region=(1315,833,1745,995))
    eg = pg.locateCenterOnScreen(r'images/ElectroGiant.png',confidence=0.9,region=(1315,833,1745,995))
    if a != None: 
        print("NOT IN BATTLE!!")
        pg.moveTo(a[0],a[1], 0.05)
        pg.click()
        
    else:
        print('IN BATTLE !!!!!')
        if p != None :
            pg.moveTo(p[0],p[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1266,1707),np.random.randint(685,767),0.05)
            pg.click()
            pass
        elif mk!= None:
            pg.moveTo(mk[0],mk[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1264,1699),np.random.randint(499,501),0.05)
            pg.click()
            pass
        elif hr!= None:
            pg.moveTo(hr[0],hr[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1264,1699),np.random.randint(499,501),0.05)
            pg.click()
            pass
        elif gg!= None:
            pg.moveTo(gg[0],gg[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1264,1699),np.random.randint(499,501),0.05)
            pg.click()
            pass
        elif eg!= None:
            pg.moveTo(eg[0],eg[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1264,1699),np.random.randint(499,501),0.05)
            pg.click()
            pass
        elif rg!= None:
            pg.moveTo(rg[0],rg[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1264,1699),np.random.randint(499,501),0.05)
            pg.click()
            pass
        elif mw!= None:
            pg.moveTo(mw[0],mw[1], 0.05)
            pg.click()
            #if a == 1:
            pg.moveTo(np.random.randint(1266,1707),np.random.randint(685,767),0.05)
            #else:
            #    pg.moveTo(np.random.randint(1541,),np.random.randint(688,767),0.05)
            pg.click()
            pass
        elif mh!= None:
            pg.moveTo(mh[0],mh[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1400,1500),np.random.randint(600,700),0.05)
            pg.click()
            pass
            pass
        elif ok!= None:
            pg.moveTo(ok[0],ok[1], 0.05)
            pg.click()
            pg.moveTo(np.random.randint(1264,1699),np.random.randint(499,501),0.05)
            pg.click()
            pass