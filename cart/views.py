"""Module providingFunction for Decimal conversion"""
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect
from Item import views
from Item.models import Item
from cart.cart import Cart


def add_to_cart1(request):
    """View access the add_item function of cart class to add the item into the cart"""
    item_id  = request.POST['item_id']    
    item = Item.objects.get(id=item_id) 
    if not item.is_retired:
        cart = Cart(request)
        cart.add_item(item)
        messages.success(request, "Item has been added into the cart")
    else:
        messages.info(request, "Sorry the item is not available at this moment.")
    item_list = views.Item_Handler()
    response = item_list.get(request)
    return response


def view_cart(request):
    """Displays the cart to user"""
    cart = Cart(request)
    cart_items = cart.get_items()
    total_price = cart.get_total()
    tax_pay = int((total_price/100)*17)
    grand_total = total_price + tax_pay
    try:
        for item_id, item_data in cart_items:
            item_data['sub_total'] = Decimal(item_data['quantity']) * Decimal(item_data['price'])
            item = Item.objects.get(pk = int(item_id))
            item_data['photo'] = item.photo.url
        print(cart_items, "---")
    except Item.DoesNotExist as e:
        print(e)
        messages.error(request, "Not found")
    return render(request, 'cart.html', 
                  {'cart_items': cart_items, 'total_price': total_price, 'tax_pay': tax_pay, 'gt': grand_total})


def clear_cart(request):
    """view that utilizes cart.clear() to remove all the items from the cart"""
    cart = Cart(request)
    try:
        cart.clear()
        messages.success(request, "All the items have been cleared")
    except Exception as e:
        print(e)
        messages.error(request,"Cannot clear the cart")

    return redirect('cart_view')


def removeitem(request):
    """view removes an item from the cart"""
    cart = Cart(request)
    item_id = int(request.POST['item_id'])

    try:
        item = Item.objects.get(pk = item_id)
        print(item)
        cart.remove_item(item)
        messages.success(request, "Item has been removed from the cart")
    except Exception as e:
        print(e)
        messages.warning(request, "Could not found the item")

    return redirect('cart_view')

def remove_quantity(request):
    """view decreases the quantity of the item by 1"""
    cart = Cart(request)
    item_id = int(request.POST['item_id'])
    try:
        item = Item.objects.get(pk = item_id)
        cart.remove_quantity(item)
    except Exception as e:
        print(e)
    return redirect('cart_view')
    
def add_quantity(request):
    """View increases the quantity of the item by 1"""
    cart = Cart(request)
    item_id = int(request.POST['item_id'])
    try:
        item = Item.objects.get(pk = item_id)
        cart.add_quantity(item)
    except Exception as e:
        print(e)
    return redirect('cart_view')
