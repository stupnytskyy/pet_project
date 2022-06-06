
import sys
sys.path.append('./src/objects')
sys.path.append('./src/locators')
import locators
import base_page

# from src.locators import locators
# from src.objects import base_page


def click_sign_in_button ():
    try:
        base_page.click_button(locators.SIGN_IN_BUTTON_1)
    except Exception: pass
# try:
#    base_page.click_button(locator.SIGN_IN_BUTTON_11)
#    except Exception: pass

def click_confirm_sign_in_button ():
    base_page.click_button(locators.SIGN_IN_BUTTON_2)

def type_email ():
    base_page.type_text(locators.EMAIL_FIELD, locators.EMAIL)

def click_next_button ():
    base_page.click_button(locators.NEXT_BUTTON)

def type_password ():
    base_page.type_text(locators.PASSWORD_FIELD, locators.PASSWORD)

def click_yes_button ():
    base_page.click_button(locators.YES_BUTTON)


def type_search_word ():
    base_page.type_text(locators.SEARCH_FIELD, base_page.selection_randomizer())

def click_search_button ():
    base_page.click_button(locators.SEARCH_BUTTON)