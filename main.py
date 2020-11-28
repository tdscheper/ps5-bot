from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

def main():
    add2Cart = "//button[@data-tl-id='ProductPrimaryCTA-cta_add_to_cart_button']"
    checkout = "//button[@data-automation-id='pac-pos-proceed-to-checkout']"
    continueAsGuest = "//button[@data-automation-id='new-guest-continue-button']"
    continueAfterPickupPlace = "//button[@data-automation-id='fulfillment-continue']"
    pickupPersonFirstName = "//input[@data-automation-id='primary-pickup-first-name']"
    pickupPersonLastName = "//input[@data-automation-id='primary-pickup-last-name']"
    pickupPersonEmail = "//input[@data-automation-id='primary-pickup-email']"
    continueAfterPickupPerson = "//button[@data-automation-id='pickup-submit']"
    cardInput = "//input[@name='creditCard']"
    cvvInput = "//input[@name='cvv']"
    phoneInput = "//input[@name='phone']"
    billingStreetInput = "//input[@name='addressLineOne']"
    cardMonthDropdown = "//select[@name='month-chooser']" # text:"MM"
    cardYearDropdown = "//select[@name='year-chooser']" # text:"YY"
    reviewOrder = "//button[@data-automation-id='save-cc']"
    placeOrder = "//button[@class='button auto-submit-place-order no-margin set-full-width-button pull-right-m place-order-btn btn-block-s button--primary']"

    clickButton(add2Cart)
    clickButton(checkout)
    clickButton(continueAsGuest)
    clickButton(continueAfterPickupPlace)
    enterKeys(pickupPersonFirstName, "ADD_FIRST_NAME_HERE")
    enterKeys(pickupPersonLastName, "ADD_LAST_NAME_HERE")
    enterKeys(pickupPersonEmail, "ADD_EMAIL_HERE")
    clickButton(continueAfterPickupPerson)
    enterKeys(cardInput, "ADD_CARD_NUMBER_HERE")
    enterKeys(cvvInput, "ADD_CARD_CVV_HERE")
    enterKeys(phoneInput, "ADD_PHONE_NUMBER_HERE")
    enterKeys(billingStreetInput, "ADD_STREET_ADDRESS_HERE")
    selectFromDropdown(cardMonthDropdown, "ADD_CARD_EXPIRATION_MONTH_HERE") 
        #Ex: If month is January of 2021, use 01 
    selectFromDropdown(cardYearDropdown, "ADD_CARD_EXPIRATION_YEAR_HERE")
        #Ex: If month is January of 2021, use 21
    clickButton(reviewOrder)
    clickButton(placeOrder)

def clickButton(button):
    try:
        driver.find_element_by_xpath(button).click()
        pass
    except Exception:
        time.sleep(1)
        clickButton(button)

def enterKeys(input, keys):
    try:
        driver.find_element_by_xpath(input).send_keys(keys)
        pass
    except Exception:
        time.sleep(1)
        enterKeys(input, keys)

def selectFromDropdown(dropdown, text):
    try:
        driver.find_element_by_xpath(dropdown + "/option[text()='" + text + "']")
        pass
    except Exception:
        time.sleep(1)
        selectFromDropdown(dropdown, text)

if __name__ == '__main__':
    # start up Chrome
    chrome_options = Options()
    chrome_options.binary_location = 'ADD_PATH_TO_CHROME_HERE'
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        options = chrome_options
    )

    # go to PS5 on Walmart
    driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")
    time.sleep(3)

    main()