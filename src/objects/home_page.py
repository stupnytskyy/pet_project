
from locators import locators as locator
from objects import base_page as base_page


def click_sign_in_button ():
    try:
        base_page.click_button(locator.SIGN_IN_BUTTON_1)
    except Exception: pass
# try:
#    base_page.click_button(locator.SIGN_IN_BUTTON_11)
#    except Exception: pass

def click_confirm_sign_in_button ():
    base_page.click_button(locator.SIGN_IN_BUTTON_2)

def type_email ():
    base_page.type_text(locator.EMAIL_FIELD, locator.EMAIL)

def click_next_button ():
    base_page.click_button(locator.NEXT_BUTTON)

def type_password ():
    base_page.type_text(locator.PASSWORD_FIELD, locator.PASSWORD)

def click_yes_button ():
    base_page.click_button(locator.YES_BUTTON)


def type_search_word ():
    base_page.type_text(locator.SEARCH_FIELD, base_page.selection_randomizer())

def click_search_button ():
    base_page.click_button(locator.SEARCH_BUTTON)