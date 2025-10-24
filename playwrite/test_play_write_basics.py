import time

from playwright.sync_api import Page
def test_playwriteBasics(playwright):
   browser =  playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page = context.new_page()
   page.goto("https://google.com")

   #chromium headless mode 1 single context
def test_playwriteShortCut(page:Page):
      page.goto("https://google.com")
      assert "Google" in page.title()  # Optional validation

def test_coreLocators(page:Page):
   page.goto("https://rahulshettyacademy.com/loginpagePractise/")
   page.get_by_label("username:").fill("rahulshettyacademy")
   page.get_by_label("password:").fill("learning")
   page.get_by_role("combobox").select_option("teach")
   page.locator("#terms").check()
   page.get_by_role("link", name="terms and conditions").click()
   page.get_by_role("button", name="Sign In").click()



   time.sleep(5)

