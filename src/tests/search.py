
import sys
sys.path.append('./src/objects')
import home_page
import base_page
# from src.objects import home_page
# from src.objects import base_page
import time

time.sleep(10)
home_page.click_sign_in_button()
home_page.type_email()
home_page.click_next_button()
home_page.type_password()
home_page.click_confirm_sign_in_button()
home_page.click_yes_button()
home_page.type_search_word()
home_page.click_search_button()


time.sleep(5)
base_page.driver.close()
base_page.driver.quit()