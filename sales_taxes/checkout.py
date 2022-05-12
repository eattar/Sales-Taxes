from sales_taxes.shopping_basket import ShoppingBasket
from sales_taxes.item import Item, find_item_tax


def add_items(shopping_basket: ShoppingBasket, *items: Item):
    """Calculates item price including tax and adds it to shopping basket"""
    for item in items:
        item.unit_tax = find_item_tax(item.name) + 0.05 if item.imported else find_item_tax(item.name)
        item.total_price = item.unit_price * item.quantity * (1 + item.unit_tax)
        shopping_basket.sales_taxes += item.unit_price * item.quantity * item.unit_tax
        shopping_basket.total += item.total_price
        shopping_basket.items.append(item)


def parse_input_line(line_item):
    split_line_item = line_item.split()
    item_quantity = int(split_line_item[0])
    item_unit_price = float(split_line_item[-1])

    if 'imported' in split_line_item:
        item_name = split_line_item[1:-2]
        item_name.remove('imported')
        item_name = ' '.join(item_name)
        return Item(item_name, item_unit_price, item_quantity, True)
    else:
        item_name = split_line_item[1:-2]
        item_name = ' '.join(item_name)
        return Item(item_name, item_unit_price, item_quantity)


def round_05(number):
    """rounds number to the nearest 0.05th"""
    return 0.05 * round(number / 0.05)
