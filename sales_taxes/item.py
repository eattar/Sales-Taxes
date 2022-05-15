from sales_taxes.round_up_to_nearest_05 import roundup_nearest_05


INVALID_INPUT = """Invalid input! Follow this pattern:
                 [Item Quantity] imported[optional] [Item Name] at [Item Price]
                 Example: 1 imported box of chocolates at 10.00  
                 Example: 1 music CD at 14.99"""


class Item:
    """ class for items added to shopping basket"""
    def __init__(self, name: str, unit_price: float, quantity: int, imported: bool = False,
                 unit_tax_rate: float = 0, tax: float = 0, price: float = 0) -> None:

        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.imported = imported
        self.price = price
        self.unit_tax_rate = unit_tax_rate
        self.tax = tax

    def __str__(self) -> str:
        return f'{self.quantity}{" imported" if self.imported else ""} ' \
               f'{self.name}: {(self.price + roundup_nearest_05(self.tax)):.2f}'


def parse_input_line(line_item: str) -> Item:

    split_line_item = line_item.split()

    if len(split_line_item) < 4:
        raise ValueError(INVALID_INPUT)
    if not split_line_item[-2] == 'at':
        raise ValueError(INVALID_INPUT)

    item_name = ' '.join(split_line_item[1:-2])
    if item_name.isdigit():
        raise TypeError("Invalid input! Item name must be string!")

    try:
        item_quantity = int(split_line_item[0])
    except ValueError:
        raise ValueError("Item quantity must be an integer!")

    if item_quantity <= 0:
        raise ValueError("Item quantity must be greater than zero")

    try:
        item_unit_price = float(split_line_item[-1])
    except ValueError:
        raise ValueError("Invalid input! Item unit price must be a digit!")
    if item_unit_price <= 0:
        raise ValueError("Invalid input! Item unit price must not be equal or less than zero!")

    if 'imported' in split_line_item:
        item_name = split_line_item[1:-2]
        item_name.remove('imported')
        item_name = ' '.join(item_name)
        return Item(item_name, item_unit_price, item_quantity, True)
    else:
        item_name = split_line_item[1:-2]
        item_name = ' '.join(item_name)
        return Item(item_name, item_unit_price, item_quantity)


def find_item_unit_tax_rate(name: str) -> float:

    if name in ['book', 'box of chocolates', 'chocolate bar', 'packet of headache pills']:
        return 0
    else:
        return 0.10
