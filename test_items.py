link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test__see_basket_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), 'Кнопка добавить в корзину не найдена'
