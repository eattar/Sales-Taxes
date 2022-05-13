from sales_taxes.shopping_basket import ShoppingBasket
from sales_taxes.item import parse_input_line
from sales_taxes.round_up_to_nearest_05 import roundup_nearest_05


def main():

    shopping_basket = ShoppingBasket()

    while True:

        line_item = input("Enter: ")

        if line_item == 'y':
            break

        item = parse_input_line(line_item)

        shopping_basket.add_items(item)

    for item in shopping_basket.items:
        print(f'{item.quantity} {"imported" if item.imported else ""} {item.name}: {round(item.price, 2)}')
    print(f'Sales taxes: {roundup_nearest_05(shopping_basket.total_sales_taxes()):.2f}')
    print(f'Total: {round(shopping_basket.total_price(), 2):.2f}')


if __name__ == '__main__':
    main()
