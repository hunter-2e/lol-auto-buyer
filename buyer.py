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

coords = auto.locateCenterOnScreen("fountain.png", confidence=.3)
auto.click(coords)
print(captureChat())

while 1:
    if keyboard.read_key() == 'b':
        print("pressed b")
        auto.sleep(3)
        


