from locators.order_page_locators import OrderPageLocators


class OrderTestData:
    CASE_1 = {
        "name": "Юлия",
        "surname": "Дементьева",
        "address": "Улица Ленина, дом 11",
        "phone_number": "79009009090",
        "scooter_color": OrderPageLocators.BLACK_PEARL_CHECKBOX,
        "comment": "как можно скорее"
    }

    CASE_2 = {
        "name": "Мария",
        "surname": "Петров",
        "address": "улица Ленина, дом 21",
        "phone_number": "78008008080",
        "scooter_color": OrderPageLocators.GRAY_HOPELESSNESS,
        "comment": "Спасибо"
    }
