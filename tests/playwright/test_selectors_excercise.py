from pathlib import Path
import re
from playwright.sync_api import Page, expect

LOCAL_HTML = (Path(__file__).parent / "src" / "playwright-selectors.html").as_uri()
print(f"Local HTML file path: {LOCAL_HTML}")

# TODO: Find the button using its role and name.
# TODO: Click it and verify the confirmation text.
def test_button_click(page: Page):
    page.goto(LOCAL_HTML)
    button = page.get_by_role("button", name="Open Details")
    button.highlight()
    button.click()
    confirmation_text = page.get_by_text("Button clicked!")
    expect(confirmation_text).to_be_visible()

# TODO: Find the email input using its placeholder.
def test_inputs(page: Page):
    page.pause()
    page.goto(LOCAL_HTML)
    email_input = page.get_by_placeholder("name@example.com")
    
    email_input.highlight()
    assert email_input.is_visible(), "Email input field is not visible."
    email_input.fill("yashago@gmail.com")

    password_input = page.get_by_placeholder("Enter your password")
    password_input.scroll_into_view_if_needed()
    # TODO: Fill in the password field.        
    password_input.highlight()
    password_input.fill("securepassword123")
    assert password_input.is_visible(), "Password input field is not visible."

    # TODO: Select United Kingdom from the dropdown.
    dropdown = page.locator("#country")
    dropdown.scroll_into_view_if_needed()
    dropdown.highlight()
    dropdown.select_option("United Kingdom")
    expect(dropdown).to_be_visible()

    # TODO: Select Premium.
    premium = page.get_by_label("Premium")
    expect(premium).to_be_visible()
    premium.scroll_into_view_if_needed()
    premium.highlight()

    # TODO: Check the terms checkbox.
    terms_checkbox = page.get_by_label("terms")
    terms_checkbox.scroll_into_view_if_needed()
    terms_checkbox.check()
    terms_checkbox.highlight()
    expect(terms_checkbox).to_be_visible()

    # TODO: Submit the form and verify the confirmation.
    submit_button = page.get_by_role("button", name=re.compile(r"^Submit Form$"))
    submit_button.scroll_into_view_if_needed()
    submit_button.highlight()
    submit_button.click()

    submission_text = "Form submitted successfully!"
    expect(page.get_by_text(submission_text)).to_be_visible()

    # TODO: Click the Details link and verify that a new tab opens.
    detailsLink = page.get_by_role("link", name="Go to Details Page")
    detailsLink.scroll_into_view_if_needed()
    detailsLink.highlight()
    detailsLink.click()

    # TODO: Verify the headline and paragraph on the new page.
    headline = page.get_by_role("heading", level=1, name="Playwright")
    expect(headline).to_be_visible()