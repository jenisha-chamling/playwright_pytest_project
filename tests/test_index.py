from playwright.sync_api import Page, expect
 
 # verification of url
def test_verifyUrl(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  expect(page).to_have_url("http://localhost/php_practice/index.php")
  page.wait_for_timeout(2000)

#verification  of title
def test_verifyTitle(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  expect(page).to_have_title("Student Registration Form")
  page.wait_for_timeout(2000)

#to get the title
def test_getTitle(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  Title= page.title()
  print(f"Title of the webpage is {Title}")
 
# Positive testing 
def test_form_submission_success(page: Page):
  page.goto("http://localhost/php_practice/index.php")

  page.fill("input[name='first']", "Neha")
  page.fill("input[name='last']", "Sha")
  page.fill("input[name='grade']", "3")

  page.click("input[name='submit']")

  expect(page.get_by_text("Student enrollment successful")).to_be_visible()
  page.wait_for_timeout(5000)


# Negative testing 
def test_empty_form_validation(page: Page):
  page.goto("http://localhost/php_practice/index.php")

  page.click("input[name='submit']")

  expect(page.get_by_text("Enter your first name")).to_be_visible()
  page.wait_for_timeout(5000)


  #Verify all form fields are visible
def test_form_elements_present(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    expect(page.locator("input[name='first']")).to_be_visible()
    expect(page.locator("input[name='last']")).to_be_visible()
    expect(page.locator("input[name='grade']")).to_be_visible()
    expect(page.locator("input[name='submit']")).to_be_visible()

  # Test only first name missing
def test_first_name_required(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='last']", "Shah")
    page.fill("input[name='grade']", "3")

    page.click("input[name='submit']")

    expect(page.get_by_text("Enter your first name")).to_be_visible()

    #Test only last name missing
def test_last_name_required(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='first']", "Neha")
    page.fill("input[name='grade']", "3")

    page.click("input[name='submit']")

    expect(page.get_by_text("Enter your last name")).to_be_visible()

# Test only grade missing
def test_grade_required(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='first']", "Neha")
    page.fill("input[name='last']", "Shah")

    page.click("input[name='submit']")

    expect(page.get_by_text("Enter your grade")).to_be_visible()
  
#Verify form fields accept entered data
def test_input_values(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='first']", "John")

    expect(page.locator("input[name='first']")).to_have_value("John")

    
