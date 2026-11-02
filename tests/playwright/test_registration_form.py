from playwright.sync_api import Page, expect
from tests.playwright.consts import REGISTRATION_FORM

GITHUB_FORM_URL = "https://github.com/yashago/hadasim-qa-pytest/blob/9bcef875b222092b4f32c3599b7773e5d1aca48b/tests/playwright/src/playwright_registration_form.html"
FILE_PATH = f"https://htmlpreview.github.io/?{GITHUB_FORM_URL}"

def test_registration_form(page: Page):
    # Navigate to the local registration form
    page.goto(FILE_PATH)
    printAccessibilityTree(page)

    page.pause()

    fillInFullForm(page)
    #validateResetForm(page)
    #fillInFullForm(page)
    #validateSubmitForm(page)
    pass

def test_header(page: Page):
    page.goto(FILE_PATH)
    # testRegistrationLink(page)
    # testPreferencesLink(page)
    testHelpLink(page)
    # testPlaywrightDocsLink(page)

def fillInFullForm(page):
    #TODO: Fill in the first name
    fillInFirstName(page, "John")

    #TODO: Fill in the last name
    # fillInLastName(page, "Doe")

    #TODO: Fill in the email
    # fillInEmail(page, "your@email.com")

    #TODO: Fill in the email confirmation
    # fillInEmailConfirmation(page, "your@email.com")

    #TODO: Fill in the password
    # fillInPassword(page, "yourpassword")

    #TODO: Fill in the phone number
    # fillInPhoneNumber(page, "+972-54-4746095")

    #TODO: Fill in the date of birth
    fillInDateOfBirth(page, "1990-01-01")

    #TODO: Select the country
    # selectCountry(page, "United States")

    #TODO: Fill in the city
    # fillInCity(page, "Beer-Sheva")

    #TODO: Select the gender
    # selectGender(page, "Female")

def printAccessibilityTree(page):
    pageAccesibility = page.locator("body").aria_snapshot()
    print(f"pageAccesibility: {pageAccesibility}")

def fillInFirstName(page, firstName):
    #By role, preferred method
    page.get_by_role("textbox", name="First name").fill("John")
    
    #By label, preferred method
    page.get_by_label("First name").fill("Doe")

    #By placeholder, good option if the placeholder is unique and descriptive
    page.get_by_placeholder("e.g. Alex").fill("John")

    #By locator, good option if the locator is unique and descriptive
    page.locator("#firstName").fill("Doe")

    #By locator, Usually unnecessary
    page.locator('input[id="firstName"]').fill("John")
    page.fill('input[name="firstName"]', "Doe")

def fillInDateOfBirth(page, dateOfBirth):
    #By label, preferred method
    datePicker = page.get_by_label("Date of birth")
    datePicker.fill(dateOfBirth)
    datePicker.scroll_into_view_if_needed()
    datePicker.highlight()  

def testRegistrationLink(page):
    registrationLink = page.get_by_role("link", name="Registration")
    registrationLink.scroll_into_view_if_needed()
    registrationLink.highlight()
    registrationLink.click()
    printAccessibilityTree(page)

    dialog = page.get_by_role("dialog", name="Help")
    expect(dialog).to_be_visible()


def testHelpLink(page):
    helpLink = page.get_by_role("link", name="Help")
    helpLink.scroll_into_view_if_needed()
    helpLink.highlight()
    helpLink.click()

    printAccessibilityTree(page)
    dialog = page.get_by_role("dialog", name=REGISTRATION_FORM["modalHeaderText"])
    expect(dialog).to_be_visible()
    expect(dialog.get_by_role("heading", level=2, name=REGISTRATION_FORM.get("modalHeaderText"))).to_be_visible()

    dialogOkButton = dialog.get_by_role("button", name=REGISTRATION_FORM.get("modalButtonText"))
    expect(dialogOkButton).to_be_visible()
    expect(dialogOkButton).to_be_enabled()
    dialogOkButton.click()