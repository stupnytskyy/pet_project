import Src.Locators.locators as locators
import Src.Objects.base_page as base_page
from decouple import config
EMAIL = config('EMAIL', default='')
PASSWORD = config('PASSWORD', default='')


def click_sign_in_button():
    try:
        base_page.click_button(locators.SIGN_IN_BUTTON_1)
    except Exception: pass


def click_confirm_sign_in_button():
    base_page.click_button(locators.SIGN_IN_BUTTON_2)


def type_email():
    base_page.type_text(locators.EMAIL_FIELD, EMAIL)


def click_next_button():
    base_page.click_button(locators.NEXT_BUTTON)


def type_password():
    base_page.type_text(locators.PASSWORD_FIELD, PASSWORD)


def click_yes_button():
    base_page.click_button(locators.YES_BUTTON)


def type_search_word():
    base_page.type_text(locators.SEARCH_FIELD, base_page.selection_randomizer())


def click_search_button():
    base_page.click_button(locators.SEARCH_BUTTON)