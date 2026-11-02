import re
import pytest
from playwright.sync_api import Page, expect, Browser
from utils import login_pipeline

def test_has_title(page: Page):
    page.goto("http://localhost:3000/")
    expect(page).to_have_title(re.compile("OWASP Juice Shop"))


def test_login(page: Page):
    login_pipeline(page)
    expect(page).to_have_url("http://localhost:3000/#/search")

    
    # Salvando o estado do teste, evitando que seja necessário logar novamente
    page.context.storage_state(path="state.json")
    
#Teste criado usando a ferramente de geração automática de código do Playwright
def test_ai_chat(py_page: Page):
    page = py_page
    
    page.goto("http://localhost:3000/")
    page.get_by_role("button", name="Open Sidenav").click()
    page.get_by_role("link", name="Go to AI chat page").click()
    
    textbox = page.get_by_role("textbox", name="Ask me anything")
    textbox.click()
    textbox.fill("Hello.")
    textbox.press("Enter") 
    
    expect(page.locator(".assistant")).to_be_visible()
    
    chat_response = page.locator(".assistant")
    
    expect(chat_response).not_to_be_empty(timeout=15000)
    

def test_add_item_to_basket(page: Page):
    login_pipeline(page)
    
    page.get_by_role("article").filter(has_text="Apple Juice (1000ml) 1.99¤").get_by_label("Add to Basket").click()
    page.get_by_role("button", name="Show the shopping cart").click()
    expect(page.get_by_role("row", name="Apple Juice (1000ml) Apple")).to_be_visible()


def test_remove_item_from_basket(page: Page):
    login_pipeline(page)
    
    page.get_by_role("article").filter(has_text="Apple Juice (1000ml) 1.99¤").get_by_label("Add to Basket").click()
    page.get_by_role("button", name="Show the shopping cart").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    expect(page.get_by_role("row", name="Apple Juice (1000ml) Apple")).not_to_be_visible()

def test_checkout(page: Page):
    login_pipeline(page)
    
    page.get_by_role("article").filter(has_text="Apple Juice (1000ml) 1.99¤").get_by_label("Add to Basket").click()
    page.get_by_role("button", name="Show the shopping cart").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("cell").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("button", name="Proceed to payment selection").click()
    page.get_by_role("cell").first.click()
    page.get_by_role("button", name="Proceed to delivery method").click()
    page.get_by_role("cell").first.click()
    page.get_by_role("row", name="************4368").get_by_label("", exact=True).check()
    page.get_by_role("button", name="Proceed to review").click()
    page.get_by_role("button", name="Complete your purchase").click()
    expect(page.get_by_role("heading")).to_contain_text("Thank you for your purchase!")

def test_complaint(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.get_by_role("button", name="Open Sidenav").click()
    page.get_by_role("link", name="Go to complain page").click()
    page.get_by_role("textbox", name="Field for entering the").click()
    page.get_by_role("textbox", name="Field for entering the").fill("Não gostei do serviço.")
    page.get_by_role("button", name="Button to send the complaint").click()
    expect(page.locator("section")).to_contain_text("Customer support will get in touch with you soon! Your complaint reference is #")
    
    
def test_see_reviews(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.locator("section").filter(has_text="Apple Juice (1000ml)").click()
    expect(page.locator("mat-dialog-content")).to_be_visible()
    page.get_by_role("button", name="Reviews (").click()
    expect(page.get_by_role("region", name="Reviews (")).to_contain_text("One of my favorites!")
    
    
def test_write_reviews(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.locator("section").filter(has_text="Apple Juice (1000ml)").click()
    page.get_by_role("textbox", name="Text field to review a product").click()
    page.get_by_role("textbox", name="Text field to review a product").fill("Muito bom.")
    page.get_by_role("button", name="Send the review").click()
    page.get_by_role("heading", name="Write a review").click()
    expect(page.get_by_text("You review has been saved.")).to_be_visible()
    page.get_by_role("button", name="Reviews (").click()
    expect(page.get_by_role("region", name="Reviews (")).to_contain_text("Muito bom.")
    
    
def test_search_function(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.get_by_role("button", name="Open search").click()
    page.get_by_role("textbox").fill("OWASP Juice Shop Sticker Page")
    page.get_by_role("textbox").press("Enter")
    expect(page.locator("div").filter(has_text="OWASP Juice Shop Sticker Page 9.99¤ add_shopping_cart Add to Basket")).to_be_visible()
    expect(page.get_by_text("– 1 of 1")).to_be_visible()
    
    

    
def test_change_username(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.get_by_role("button", name="Show/hide account menu").click()
    page.get_by_role("menuitem", name="Go to user profile").click()
    page.get_by_role("textbox", name="Text field for the username").click()
    page.get_by_role("textbox", name="Text field for the username").fill("TestUsername")
    page.get_by_role("button", name="Button to save/set the").click()
    expect(page.get_by_role("textbox", name="Text field for the username")).to_have_value("TestUsername")
    
    
def test_track_order(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.get_by_role("button", name="Show/hide account menu").click()
    page.get_by_role("menuitem", name="Show Orders and Payment Menu").hover()
    page.get_by_role("menuitem", name="Go to order history page").click()
    page.get_by_role("button", name="Track Your Order").first.click()
    expect(page.locator("mat-card")).to_contain_text("Expected Delivery")

    # ---------------------
    
    
def test_change_password(py_page: Page):
    page = py_page
    page.goto("http://localhost:3000/")

    page.get_by_role("button", name="Show/hide account menu").click()
    page.get_by_role("menuitem", name="Show Privacy and Security Menu").hover()
    page.get_by_role("menuitem", name="Go to change password page").click()
    page.get_by_role("textbox", name="Field to enter the current").fill("admin123")
    page.get_by_role("textbox", name="Field for the new password").fill("admin123")
    page.get_by_role("textbox", name="Field to repeat the new").fill("admin123")
    page.get_by_role("button", name="Button to confirm the change").click()
    expect(page.get_by_role("status")).to_contain_text("Your password was successfully changed.")
    page.get_by_role("button", name="Show/hide account menu").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.get_by_role("button", name="Show/hide account menu").click()
    page.get_by_role("menuitem", name="Go to login page").click()
    page.get_by_role("textbox", name="Text field for the login email").click()
    page.get_by_role("textbox", name="Text field for the login email").fill("admin@juice-sh.op")
    page.get_by_role("textbox", name="Text field for the login password").click()
    page.get_by_role("textbox", name="Text field for the login password").fill("admin123")
    page.get_by_role("button", name="Login", exact=True).click()
    expect(page).to_have_url("http://localhost:3000/#/search")


    # ---------------------
