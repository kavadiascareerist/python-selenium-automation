from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_FORM = (By.ID, "login")

    def is_sign_in_form_displayed(self):
        return self.presence_of_element(*self.SIGN_IN_FORM)
