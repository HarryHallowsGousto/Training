from decimal import Decimal

import pytest
from src.checkout import CheckOut, Item, Rules


@pytest.mark.parametrize(
    "shopping_list,total_price",
    [
        [
            [
                Item(
                    name="Apple",
                    price=Decimal(0.5).quantize(Decimal('0.01')),
                ),
                Item(
                    name="Banana",
                    price=Decimal(0.3).quantize(Decimal('0.01')),
                ),
                Item(
                    name="Chocolate",
                    price=Decimal(0.2).quantize(Decimal('0.01')),

                ),
                Item(
                    name="Doritos",
                    price=Decimal(0.15).quantize(Decimal('0.01')),
                ),
            ],
            Decimal(1.15).quantize(Decimal('0.01'))
        ],
        [
            [
                Item(
                    name="Apple",
                    price=Decimal(0.5).quantize(Decimal('0.01')),
                ),
                Item(
                    name="Banana",
                    price=Decimal(0.3).quantize(Decimal('0.01')),
                ),
                Item(
                    name="Chocolate",
                    price=Decimal(0.2).quantize(Decimal('0.01')),
                ),
            ],
            Decimal(1.0).quantize(Decimal('0.01'))
        ]
    ]
)
def test_scanned_item(shopping_list, total_price):
    # Arrange
    checkout = CheckOut(rules=None)

    # Act
    for item in shopping_list:
        checkout.scan(item)

    # Assert
    assert checkout.calculated_total_price() == total_price


def test_special_offers_for_single_item():
    # Arrange
    shopping_list = [
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01')),
        ),
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01')),
        ),
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01')),
        ),
    ]

    pricing_rules = Rules(
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01'))
        ),
        offer_quantity=3,
        discount=Decimal(33.33).quantize(Decimal('0.01'))
    )

    checkout = CheckOut(rules=pricing_rules)

    # Act
    for item in shopping_list:
        checkout.scan(item)

    # Assert
    assert checkout.calculated_total_price() == 1.00


'''
@pytest.mark.parametrize(
    "shopping_list,rules,total_price",
    [
        [  # Iteration
            [  # Shopping List
                Item(
                    name='Apple',
                    price=Decimal(0.5).quantize(Decimal('0.01')),
                ),
                Item(
                    name='Apple',
                    price=Decimal(0.5).quantize(Decimal('0.01')),
                ),
            ],
            [  # Rules
                Rules(
                    Item(
                        name='Apple',
                        price=Decimal(0.5).quantize(Decimal('0.01'))
                    ),
                    offer_quantity=3,
                    discount=Decimal(33.33).quantize(Decimal('0.01'))
                )
            ],  # Total Price
            Decimal(1.00).quantize(Decimal('0.01')),
        ]
    ]
)
'''


def test_special_offers_for_multiple_items():
    # Arrange
    shopping_list = [
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01')),
        ),
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01')),
        ),
        Item(
            name='Banana',
            price=Decimal(0.25).quantize(Decimal('0.01')),
        ),
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01')),
        ),
    ]

    rules = Rules(
        Item(
            name='Apple',
            price=Decimal(0.5).quantize(Decimal('0.01'))
        ),
        offer_quantity=3,
        discount=Decimal(33.33).quantize(Decimal('0.01'))
    )
    total_price = 1.25

    checkout = CheckOut(rules=rules)

    # Act
    for item in shopping_list:
        checkout.scan(item)

    # Assert
    assert checkout.calculated_total_price() == total_price
