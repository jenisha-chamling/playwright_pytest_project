from playwright.sync_api import Page, expect
 
 # assertion of url
def test_verifyUrl(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  expect(page).to_have_url("http://localhost/php_practice/index.php")
  page.wait_for_timeout(2000) #for debugging

#assertion of title
def test_verifyTitle(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  expect(page).to_have_title("Student Registration Form")
  page.wait_for_timeout(2000) #for debugging

#to get the title
def test_getTitle(page:Page):
  page.goto("http://localhost/php_practice/index.php")
  Title= page.title()
  print(f"Title of the webpage is {Title}")

 
# Positive testing 
def test_form_submission_success(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    textbox = page.get_by_role("textbox", name="First Name")

    expect(textbox).to_be_visible()

    textbox.fill("Christina")
    page.wait_for_timeout(2000) #for debugging


# Negative testing 
def test_empty_form_validation(page: Page):
  page.goto("http://localhost/php_practice/index.php")

  page.get_by_role("button", name="Register").click()

  expect(page.get_by_text("Enter your first name")).to_be_visible()
  page.wait_for_timeout(5000) #for debugging


  #Smoke testing after addition of Roll No. in the registration form 
def test_form_elements_present(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    expect(page.locator("input#fname")).to_be_visible()
    expect(page.locator("input#lname")).to_be_visible()
    expect(page.locator("input#female")).to_be_enabled()

    expect(page.locator("input[name='grade']")).to_be_visible()
    expect(page.locator("input[name='roll']")).to_be_visible()
    expect(page.locator("input[name='submit']")).to_be_visible()


  # Regression testing TC1
def test_first_name_required(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='last']", "Shah")
    page.fill("input[name='grade']", "3")
    page.fill("input[name='roll']","11")

    page.click("input[name='submit']")

    expect(page.get_by_text("Enter your first name")).to_be_visible()
    page.wait_for_timeout(2000) #for debugging


  # Regression testing TC2
def test_last_name_required(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='first']", "Neha")
    page.fill("input[name='grade']", "3")
    page.fill("input[name='roll']","12")

    page.click("input[name='submit']")

    expect(page.get_by_text("Enter your last name")).to_be_visible()
    

# Regression testing TC3
def test_grade_required(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='first']", "Neha")
    page.fill("input[name='last']", "Shah")
    page.fill("input[name='roll']","13")

    page.click("input[name='submit']")

    expect(page.get_by_text("Enter your grade")).to_be_visible()
  
# Regression testing TC4
def test_input_values(page: Page):
    page.goto("http://localhost/php_practice/index.php")

    page.fill("input[name='first']", "John")

    expect(page.locator("input[name='first']")).to_have_value("John")


    
    
