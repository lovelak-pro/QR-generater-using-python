import pyqrcode
from pyautogui import prompt
import random
site_link = prompt('Enter your URL','QR Code Generator in python')
url = pyqrcode.create(site_link)
names = random.randrange(1000,100000)
url.png(f'QR-{names}.png', scale=15)
