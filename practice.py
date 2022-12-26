"""
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome

driver = Chrome()
driver.get("example.com")
def alert(msg):
    logging.info(msg)

def select(driver):
    radio = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'c30a6d7b-4ae9-43fe-881a-1e0d5f7e1153')))
    vote_btn = driver.find_element(By.CSS_SELECTOR, '.totalpoll-button totalpoll-button-primary totalpoll-buttons-vote')
    driver.execute_script("arguments[0].style.height='50px';", vote_btn)
    back_btn = driver.find_element(By.CSS_SELECTOR,".ccchildpage  ccfirst ccodd ccpage-count-3 ccpage-id-3878 ccpage-abia-state ccpage-has-parent ccpage-pid-3577 ccpage-parent-gubernetorial-candidates".get_attribute('href'))
    return radio, vote_btn,back_btn

def event_fire(driver, element, event_type):
    try:
        element.click()
    except Exception:
        logging.exception('Could not fire event')

def main():
    driver = webdriver.Chrome()
    try:
        while True:
            radio, vote_btn, back_btn = select(driver)
            event_fire(driver, radio, 'click')
            event_fire(driver, vote_btn, 'click')
            WebDriverWait(driver, 100).until(EC.staleness_of(vote_btn))
            event_fire(driver, back_btn, 'click')
            WebDriverWait(driver, 100).until(EC.staleness_of(back_btn))
    except Exception:
        logging.exception('Error during main loop')
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
time.sleep(5)
"""

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
driver = Chrome()
good = Chrome()
driver.get('https://nigeriansdecide.com/wp-admin/admin-ajax.php?action=totalpoll&totalpoll%5BpollId%5D=3875&totalpoll%5Baction%5D=view&totalpoll%5Bscreen%5D=vote')
#driver.get("https://nigeriansdecide.com/gubernetorial-candidates/abia-state/")
good.get('https://nigeriansdecide.com/gubernetorial-candidates/abia-state/')
def alert(msg):
    logging.info(msg)

def select(driver):
    radio = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'c30a6d7b-4ae9-43fe-881a-1e0d5f7e1153')))
    vote_btn = driver.find_element(By.CSS_SELECTOR, '.totalpoll-button.totalpoll-button-primary.totalpoll-buttons-vote')
    driver.execute_script("arguments[0].style.height='50px';", vote_btn)
    back_btn = good.find_element(By.CSS_SELECTOR, 'a.ccchildpage.ccfirst.ccodd.ccpage-count-3.ccpage-id-3878.ccpage-abia-state.ccpage-has-parent.ccpage-pid-3577.ccpage-parent-gubernetorial-candidates')
    return radio, vote_btn, back_btn

def event_fire(driver, element, event_type):
    try:
        element.click()
    except Exception:
        logging.exception('Could not fire event')

def main():
    driver = webdriver.Chrome()
    try:
        while True:
            radio, vote_btn, back_btn = select(driver)
            event_fire(driver, radio, 'click')
            event_fire(driver, vote_btn, 'click')
            WebDriverWait(driver, 100).until(EC.staleness_of(vote_btn))
            event_fire(driver, back_btn, 'click')
            WebDriverWait(driver, 100).until(EC.staleness_of(back_btn))
    except Exception:
        logging.exception('Error during main loop')
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
time.sleep(5)