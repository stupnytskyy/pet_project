
from objects import home_page as home_page
from objects import base_page as base_page
import time


home_page.click_sign_in_button()
home_page.type_email()
home_page.click_next_button()
home_page.type_password()
home_page.click_yes_button()
home_page.type_search_word()
home_page.click_search_button()


time.sleep(5)
base_page.driver.close()
base_page.driver.quit()