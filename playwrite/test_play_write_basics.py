def test_playwriteBasics(playwright):
   browser =  playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page = context.new_page()
   page.goto("https://google.com")

