import pyautogui as auto
import numpy as np
import pytesseract as tess
import cv2
from sympy import capture

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def captureGold():
    goldString = ""
    image = auto.screenshot(region=(1531,1353,86,28))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("screenshot.png", image)
    goldRead = tess.image_to_string(image)
    for letter in goldRead:
        if letter.isdigit():
            goldString += letter
    return int(goldString)

captureGold()
coords = auto.locateCenterOnScreen('fountain.png', confidence=.3)
auto.click(coords)

