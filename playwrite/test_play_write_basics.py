from playwright.sync_api import Page
def test_playwriteBasics(playwright):
   browser =  playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page = context.new_page()
   page.goto("https://google.com")

   #chromium headless mode 1 single context
   def test_playwriteShortCut(page: Page):
      page.goto("https://google.com")
      assert "Google" in page.title()  # Optional validation

