from playwright.sync_api import Page, expect

LOCAL_FORM_URL = "C:/Users/Jacob/Desktop/QA/Python/Playwright/playwright_registration_form.html"
FILE_PATH = f"file:///{LOCAL_FORM_URL}"

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
    