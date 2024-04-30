from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from random import randint

from time import sleep

# pull up edge, open up iCloud, wait for the user to log in
# swap this to whatever you want, doesn't seem to work with Firefox for me for whatever reason
driver = webdriver.Edge()
driver.get('https://www.icloud.com/')

find_my_url = 'https://www.icloud.com/find/'

# every 2 seconds, check if we've made it to the 'Find My' page
while True:
    if driver.current_url == find_my_url:
        break
    sleep(2)

# once the find my page is open in browser

# debug print statement
print("starting automation")

# wait 15 seconds for user to select the correct device
sleep(15)

# find all iframes on the page
iframes = driver.find_elements(By.TAG_NAME, 'iframe')

# loop through each iframe, i hate dynamic content
for iframe in iframes:
    try:
        driver.switch_to.frame(iframe)
        button = driver.find_element(By.CSS_SELECTOR, '.fmip-action-button.icon.play-sound-button.fm-test-playsndbtn.icloud-mouse')
        
        # if the Play Sound button is displayed, click it
        if button.is_displayed():
            while True:
                # get a random time between 30 seconds and 10 minutes
                rand_time = randint(30, 600)
                # click the button, wait that long, rinse and repeat
                button.click()
                sleep(rand_time)

        else:
            # if the button is not displayed, switch back to the main content
            driver.switch_to.default_content()

    except NoSuchElementException:
        # kinda pointless, but if the button ain't there, switch back to main content
        driver.switch_to.default_content()

# close the browser
driver.quit()
