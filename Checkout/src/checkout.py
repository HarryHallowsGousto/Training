import dataclasses
from decimal import *
from decimal import Decimal
from typing import Union


# A item = 0.50$
# B item = 0.30$
# C item = 0.20$
# D item = 0.15$

# Special Offers 
# 3 - A items = 1.30$
# 2 - B items = 0.45$


@dataclasses.dataclass
class Item:
    name: str
    price: Decimal


class CheckOut:

    def __init__(self, rules):
        self.cart = []
        self.rules = [rules]

    def scan(self, item: Item) -> None:
        self.cart.append(item)

    def cart_size(self):
        # check for individual item counts
        # iterate through items
        items = {}
        for item in self.cart:
            # Get item name and count
            if item.name in items:
                items[item.name]['item_count'] += 1
            else:
                items[item.name] = {
                    'item_count': 1,
                    'item_details': item,
                }
        return items

    @staticmethod
    def calculate_price(price, count: Decimal) -> Decimal:
        return price * count

    def calculated_total_price(self) -> Decimal:
        cart_items = self.cart_size()
        total_price = Decimal(0.0)
        for current_rule in self.rules:
            for item in cart_items.values():
                if current_rule is None:
                    total_price += self.calculate_price(
                        price=item['item_details'].price,
                        count=Decimal(item['item_count']).quantize(Decimal('0.01'))
                    )
                else:
                    special_offer = current_rule.special_offer_rules(item)
                    if special_offer is not None:
                        total_price += special_offer
                    else:
                        total_price += self.calculate_price(
                            price=item['item_details'].price,
                            count=Decimal(item['item_count']).quantize(Decimal('0.01'))
                        )
        return total_price


class Rules:
    def __init__(self, item: Item, offer_quantity, discount: Decimal):
        """
            Receives an item and a discount percentage
            These are then processed in pricing rules
        """
        self.special_offer_item = item
        self.discount = (discount / 100)
        self.offer_quantity = offer_quantity

    def special_offer_rules(self, item: dict) -> Union[Decimal, None]:
        if item['item_details'].name == self.special_offer_item.name:
            if self.offer_quantity == item['item_count']:
                current_price = item['item_details'].price * item['item_count']
                special_offer = current_price - (current_price * self.discount)
                return Decimal(special_offer).quantize(Decimal('0.01'))
        else:
            return None
