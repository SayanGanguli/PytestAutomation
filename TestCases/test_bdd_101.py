import pytest
from pytest_bdd import *


@pytest.fixture
def shopping_cart():
    return []

@given("I have an empty shopping cart")
def empty_shopping_cart(shopping_cart):
    assert len(shopping_cart) == 0

@when("I add <product> to the cart")
def add_product(shopping_cart, product):
    shopping_cart.append(product)

@then("the cart should contain <product>")
def verify_cart_contents(shopping_cart, product):
    assert product in shopping_cart