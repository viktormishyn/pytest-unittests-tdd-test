from checkout import Checkout
import pytest


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 100)
    checkout.addItemPrice('b', 200)
    return checkout


def test_canCalculateTotal(checkout):
    checkout.addItem('a')
    assert checkout.calculateTotal() == 100


def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 300


def test_canAddDiscountRule(checkout):
    checkout.addDiscount('a', 3, 200)


# @pytest.mark.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 200)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 200


def test_exceptionWithItemWithoutPrice(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')
