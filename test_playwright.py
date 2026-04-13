from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open a sample website
        page.goto("https://example.com")

        print("Page title:", page.title())

        browser.close()

if __name__ == "__main__":
    run_test()
