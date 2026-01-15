from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shopping():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductsPage(driver)
    products_page.add_to_cart("sauce-labs-backpack")
    products_page.add_to_cart("sauce-labs-bolt-t-shirt")
    products_page.add_to_cart("sauce-labs-onesie")
    products_page.go_to_cart()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("John", "Doe", "12345")
    total = checkout_page.get_total()
    
    driver.quit()
    assert total == "Total: $58.29"
