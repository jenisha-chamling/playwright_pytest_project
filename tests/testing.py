from playwright.sync_api import Page, expect
def test_verifyUrl(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  expect(page).to_have_url("http://localhost/php_practice/index.php")
  
