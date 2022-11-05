import pyautogui as auto
import numpy as np
import pytesseract as tess
import cv2
from sympy import capture
import keyboard

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def captureGold():
    goldString = ""
    image = auto.screenshot(region=(1531,1353,86,28))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("gold.png", image)
    goldRead = tess.image_to_string(image)
    for letter in goldRead:
        if letter.isdigit():
            goldString += letter
    return int(goldString)

def captureChat():
    image = auto.screenshot(region=(44,1066,487,24))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("chat.png", image)
    chatRead = tess.image_to_string(image)
    return chatRead

def getMyItems():
    #Take screenshot of items
    recallIcon = auto.locateCenterOnScreen("recall.png", confidence=.7)
    while(recallIcon == None):
        recallIcon = auto.locateCenterOnScreen("recall.png", confidence=.7)
    
    auto.moveTo(recallIcon)
    auto.moveRel(-175, -77)
    top, left = auto.position()
    myItems = auto.screenshot(region=(top, left, 156,100))
    myItems = cv2.cvtColor(np.array(myItems), cv2.COLOR_RGB2BGR)
    return myItems

wantedItems = input("Type wanted items split by ',' with no spaces after: ").split(',')
curItem = 0

while 1:
    #Wait for recall to capture screen shot of items
    keyboard.wait('b')
    curItems = getMyItems()
    cv2.imwrite('myItems.png', curItems)


    #Check if in fountain
    fountainCoords = auto.locateCenterOnScreen("fountain.png", confidence=.3)
    while(fountainCoords == None):
        fountainCoords = auto.locateCenterOnScreen("fountain.png", confidence=.3)


    #Open shop and search item then buy it
    keyboard.press('p')
    auto.sleep(.1)
    keyboard.press('l')
    auto.sleep(.1)
    auto.typewrite(wantedItems[curItem])

    searchIcon = auto.locateCenterOnScreen("searchIcon.png", confidence=.7)
    while(fountainCoords == None):
        searchIcon = auto.locateCenterOnScreen("searchIcon.png", confidence=.7)

    auto.moveTo(searchIcon)
    auto.moveRel(0,100)
    auto.mouseDown(button='right')
    auto.mouseUp(button='right')

    #Check if items did not change
    if auto.locateOnScreen('myItems.png') is None:
        keyboard.press('p')
        break



