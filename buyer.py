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

wantedItems = input("Type wanted items split by ',' with no spaces after: ").split(',')
curItem = 0

while 1:
    
    #Wait for recall
    keyboard.wait('b')

    #Check if in fountain
    fountainCoords = auto.locateCenterOnScreen("fountain.png", confidence=.3)
    while(fountainCoords == None):
        fountainCoords = auto.locateCenterOnScreen("fountain.png", confidence=.3)

    #Open shop and search item
    keyboard.press('p')
    auto.sleep(.1)
    keyboard.press('l')
    auto.sleep(.1)
    auto.typewrite(wantedItems[curItem])

    #Buy next item in list
    searchIcon = auto.locateCenterOnScreen("searchIcon.png", confidence=.7)
    while(fountainCoords == None):
        searchIcon = auto.locateCenterOnScreen("searchIcon.png", confidence=.7)

    auto.moveTo(searchIcon)
    auto.moveRel(0,100)
    auto.mouseDown(button='right')
    auto.mouseUp(button='right')

    #Take screenshot of items
    auto.moveRel(0,-100)
    auto.moveRel(721, 34)

    left, top = auto.position()
    itemTree = auto.screenshot(region=(left, top, 453, 374))
    itemTree = cv2.cvtColor(np.array(itemTree), cv2.COLOR_RGB2BGR)
    cv2.imwrite('itemTree.png', itemTree)

    itemRead = tess.image_to_string(itemTree)
    print(itemRead)
    auto.mouseInfo()


