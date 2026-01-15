from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_id):
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
