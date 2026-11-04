from playwright.sync_api import Page
from tests.playwright.consts import FILE_PATH, REGISTRATION_FORM
import re

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_role("textbox", name="First name")
        self.last_name = page.get_by_role("textbox", name="Last name")
        self.email = page.get_by_role("textbox", name=re.compile("^"+REGISTRATION_FORM.get("formEmail")))
        self.confirmEmail = page.get_by_role("textbox", name="Confirm email")

    def open(self):
        self.page.goto(FILE_PATH)

    def fill_personal_details(self, first, last, email):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.confirmEmail.fill(email)

    def emailsAreIdentical(self):
        return self.email.input_value() == self.confirmEmail.input_value()