from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]
import re 
import pytest

PLAYWRIGHT_URL = "https://playwright.dev/"
 
def test_homepage_heading(page: Page): # pyright: ignore[reportUnknownParameterType]
    page.goto(PLAYWRIGHT_URL) # pyright: ignore[reportUnknownMemberType]
    # pageAccesibility = page.locator("body").aria_snapshot()
    # print(f"pageAccesibility: {pageAccesibility}")
    
    expect(
        page.get_by_role( # pyright: ignore[reportUnknownMemberType]
            "heading",
            level=1,
            # name="Playwright enables reliable web automation",
            #Expected to pass
            # name=re.compile("Playwright enables reliable web automation", re.IGNORECASE)
            #Expected to fail
            # name=re.compile("playwright enables reliable web automation") 
            #Expected to pass
            # name=re.compile("Playwright enables reliable web automation")
            name = re.compile("agents.$", re.IGNORECASE)
        )
    ).to_be_visible() # pyright: ignore[reportUnknownMemberType]

    # heading = page.get_by_role(
    #         "heading",
    #         name="playwright",
    #         level=1
    #     )
    # print(f"Heading: {heading}")
    # page.pause()
    # heading.highlight()
    
    # expect(heading).to_be_visible()

def test_get_started_navigation(page: Page):
    page.goto(PLAYWRIGHT_URL)
    page.pause()
    link = page.get_by_role(
        "link", name="Get started"
    )
    link.highlight()
    link.click()

    heading = page.get_by_role("heading", name="Installation")
    heading.highlight()

    expect(heading).to_be_visible()
