from sales_taxes.round_up_to_nearest_05 import roundup_nearest_05


class Item:
    """ class for items added to shopping basket"""
    def __init__(self, name: str, unit_price: float, quantity: int, imported: bool = False,
                 unit_tax_rate: float = 0, tax: float = 0, price: float = 0) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string!")
        else:
            self.name = name

        if unit_price <= 0:
            raise ValueError("Item unit price cannot be equal or less than zero!")
        elif not isinstance(unit_price, float):
            raise TypeError("Item unit price must be a float!")
        else:
            self.unit_price = unit_price

        if quantity <= 0:
            raise ValueError("Item quantity cannot be equal or less than zero!")
        elif not isinstance(quantity, int):
            raise TypeError("Item quantity must be an integer!")
        else:
            self.quantity = quantity

        self.imported = imported
        self.price = price
        self.unit_tax_rate = unit_tax_rate
        self.tax = tax

    def __str__(self):
        return f'{self.quantity}{" imported" if self.imported else ""} ' \
               f'{self.name}: {(self.price + roundup_nearest_05(self.tax)):.2f}'


def parse_input_line(line_item) -> Item:
    split_line_item = line_item.split()
    # item unit price and quantity cannot be less than or equal to zero
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


def find_item_unit_tax_rate(name) -> float:

    if name in ['book', 'chocolate bar', 'packet of headache pills', 'box of chocolates']:
        return 0
    else:
        return 0.10
