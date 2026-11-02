from playwright.sync_api import Page, expect
from tests.playwright.consts import FILE_PATH, REGISTRATION_FORM

def test_registration_form(page: Page):
    # Navigate to the local registration form
    page.goto(FILE_PATH)

    page.pause()

    fillInFullForm(page)
    validateResetForm(page)
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
    fillInFirstName(page, REGISTRATION_FORM.get("formFirstName"))

    #TODO: Fill in the last name
    fillInLastName(page, REGISTRATION_FORM.get("formLastName"))

    #TODO: Fill in the email
    # fillInEmail(page, "your@email.com")

    #TODO: Fill in the email confirmation
    # fillInEmailConfirmation(page, "your@email.com")

    #TODO: Fill in the password
    # fillInPassword(page, "yourpassword")

    #TODO: Fill in the phone number
    # fillInPhoneNumber(page, "+972-54-4746095")

    #TODO: Fill in the date of birth
    fillInDateOfBirth(page, "1984-03-03")

    #TODO: Select the country
    # selectCountry(page, "United States")

    #TODO: Fill in the city
    # fillInCity(page, "Beer-Sheva")

    #TODO: Select the gender
    selectGender(page, REGISTRATION_FORM.get("formGender"))

def validateResetForm(page):
    resetButton = page.get_by_role("button", name="Reset")
    resetButton.scroll_into_view_if_needed()
    resetButton.highlight()
    resetButton.click()
    page.get_by_text(REGISTRATION_FORM.get("resetConfirmationText")).wait_for(state="visible")
    page.get_by_text(REGISTRATION_FORM.get("resetConfirmationText")).wait_for(state="hidden")
    

    # Validate that the form fields are reset
    firstNameField = page.get_by_role("textbox", name="First name")
    expect(firstNameField).to_be_empty()

    dateOfBirthField = page.get_by_label("Date of birth")
    expect(dateOfBirthField).to_be_empty()

    genderRadioButtons = page.get_by_role("radio", name=REGISTRATION_FORM.get("formGender"))
    expect(genderRadioButtons).not_to_be_checked()

def printAccessibilityTree(page):
    pageAccesibility = page.locator("body").aria_snapshot()
    print(f"pageAccesibility: {pageAccesibility}")

def fillInFirstName(page, firstName):
    #By role, preferred method
    print(f"Filling in first name: {firstName}")
    page.get_by_role("textbox", name="First name").fill(firstName)

def fillInLastName(page, lastName):
    #By role, preferred method
    print(f"Filling in last name: {lastName}")
    page.get_by_role("textbox", name="Last name").fill(lastName)

def fillInEmail(page, email):
    #By role, preferred method
    print(f"Filling in email: {email}")
    page.get_by_role("textbox", name="Email").fill(email)

def fillInEmailConfirmation(page, emailConfirmation):
    #By role, preferred method
    print(f"Filling in email confirmation: {emailConfirmation}")
    page.get_by_role("textbox", name="Confirm email").fill(emailConfirmation)

def fillInPassword(page, password):
    #By role, preferred method
    print(f"Filling in password: {password}")
    page.get_by_role("textbox", name="Password").fill(password)

def fillInPhoneNumber(page, phoneNumber):
    #By role, preferred method
    print(f"Filling in phone number: {phoneNumber}")
    page.get_by_role("textbox", name="Phone number").fill(phoneNumber)

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
    page.pause()
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

def selectGender(page, gender):
    #By label, preferred method
    genderRadioButtons = page.get_by_role("radio", name=gender)
    genderRadioButtons.scroll_into_view_if_needed()
    genderRadioButtons.check()