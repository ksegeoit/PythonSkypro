import allure
from auth_page_allure import AuthPage
from cart_page_allure import CartPage
from main_page_allure import MainPage
from order_page_allure import OrderPage


class TestShop:
    @allure.feature("Корзина")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Добавление товара в корзину")
    @allure.description("Проверка, что товар добавляется в корзину")
    def test_add_to_cart(self, driver):
        with allure.step("Открыть страницу авторизации"):
            auth_page = AuthPage(driver)
            auth_page.open()
        with allure.step("Авторизоваться"):
            auth_page.auth("standard_user", "secret_sauce")
        with allure.step("Добавить товар в корзину"):
            main_page = MainPage(driver)
            main_page.add_first_item_to_cart()
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()
        with allure.step("Проверить, что товар в корзине"):
            cart_page = CartPage(driver)
            assert cart_page.get_items_count() == 1

    @allure.feature("Оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Оформление заказа")
    @allure.description("Проверка процесса оформления заказа")
    def test_checkout(self, driver):
        with allure.step("Открыть страницу авторизации"):
            auth_page = AuthPage(driver)
            auth_page.open()
        with allure.step("Авторизоваться"):
            auth_page.auth("standard_user", "secret_sauce")
        with allure.step("Добавить товар в корзину"):
            main_page = MainPage(driver)
            main_page.add_first_item_to_cart()
        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()
        with allure.step("Начать оформление заказа"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()
        with allure.step("Заполнить информацию"):
            order_page = OrderPage(driver)
            order_page.fill_info("Иван", "Иванов", "123456")
        with allure.step("Завершить оформление"):
            order_page.finish_order()
        with allure.step("Проверить успешное оформление"):
            assert order_page.is_order_complete()