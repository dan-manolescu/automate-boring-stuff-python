#! python3
# play2048.py - Uses selenium to control Firefox and play 2048 game in a repeating pattern.
# Requirements: Edge browser, selenium 4.9.0 and latest edge driver added to PATH.
# You can get it from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# With Firefox there are issues with latest geckodriver (0.34 at this time) as the game would not pick up the keys.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://gabrielecirulli.github.io/2048/')

buttonElem = browser.find_element(By.CSS_SELECTOR, 'button[id="ez-accept-all"]')
buttonElem.click()
time.sleep(1)

htmlElem = browser.find_element(By.TAG_NAME, 'html')
gameStatusElem = browser.find_element(By.CSS_SELECTOR, '.game-message p')
keys = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
i = 0

try:
    while gameStatusElem.text != 'Game over!':
        htmlElem.send_keys(keys[i % len(keys)])
        time.sleep(0.1)
        print('Current score is: ' + browser.find_element(By.CLASS_NAME, 'score-container').text)
        i += 1
        gameStatusElem = browser.find_element(By.CSS_SELECTOR, '.game-message p')

except KeyboardInterrupt:
    print('Interrupted! Exiting...')
    browser.close()
