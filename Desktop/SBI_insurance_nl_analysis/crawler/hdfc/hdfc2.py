from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.hdfcergo.com/about-us/financial/public-disclosures
    page.goto("https://www.hdfcergo.com/about-us/financial/public-disclosures")

    # Click text=Quarter 1
    page.locator("text=Quarter 1").click()

    # Click div[role="tabpanel"] h4 >> text=Annexure IV
    page.locator("div[role=\"tabpanel\"] h4 >> text=Annexure IV").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
