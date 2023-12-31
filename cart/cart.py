"""Module providingFunction for Decimal conversion"""
from decimal import Decimal
from django.db import transaction
from Item.models import Item
from Order.models import Order, OrderItem


class Cart:
    """Class representing a cart"""

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get("cart", {})

    def add_item(self, item, quantity=1):
        """Function that adds an item into the cart"""
        item_id = str(item.pk)
        print(item_id, "has been added to cart")
        if item_id not in self.cart:
            self.cart[item_id] = {
                "quantity": 0,
                "price": str(item.price),
                "title": str(item.title),
            }
        if item.quantity <= self.cart[item_id]["quantity"]:
            pass
        else:
            self.cart[item_id]["quantity"] += quantity
        self.save()

    def save(self):
        """Function saves an item into the cart"""
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove_item(self, item):
        """Function removes an item from the cart"""
        item_id = str(item.pk)
        print(item_id, "has been removed from the cart")
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def remove_quantity(self, item):
        """Function decreases the quantity of an item in the cart"""
        item_id = str(item.pk)
        print(item_id, "has been removed from the cart")
        if item_id in self.cart:
            if self.cart[item_id]["quantity"] > 1:
                self.cart[item_id]["quantity"] -= 1
                self.save()

    def add_quantity(self, item):
        """Function increases the quantity of an item in the cart"""
        item_id = str(item.pk)
        print(item_id, "has been removed from the cart")
        if item_id in self.cart:
            if self.cart[item_id]["quantity"] < item.quantity:
                self.cart[item_id]["quantity"] += 1
                self.save()

    def get_items(self):
        """Function returns all the items in the cart"""
        return self.cart.items()

    def clear(self):
        """Function removes all the items from the cart"""
        self.session["cart"] = {}
        self.session.modified = True

    def get_total(self):
        """Function returns the total price of items in the cart"""
        total = 0
        for item_id, item_data in self.cart.items():
            total += Decimal(item_data["price"]) * item_data["quantity"]
        return total

    def get_subtotal(self, item_id):
        """Function returns the subtotal price for every item in the cart"""
        item_data = self.cart.get(str(item_id), {})
        quantity = item_data.get("quantity", 0)
        price = Decimal(item_data.get("price", "0"))
        return quantity * price

    def create_order(self, user):
        """Function creates a new order for the user and performs this action with atomicity"""
        with transaction.atomic():
            order = Order.objects.create(user=user, status="Ordered")
            for item_id, item_data in self.cart.items():
                item = Item.objects.get(id=int(item_id))
                print(item_data)
                item.quantity = item.quantity - int(item_data["quantity"])
                if item.quantity == 0:
                    item.is_retired = True
                item.save()
                OrderItem.objects.create(
                    order=order,
                    item=item,
                    quantity=item_data["quantity"],
                    sub_total=item.price * item_data["quantity"],
                )
            self.clear()
            return order
