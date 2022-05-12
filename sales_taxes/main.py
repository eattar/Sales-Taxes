from sales_taxes.shopping_basket import ShoppingBasket
from sales_taxes.checkout import parse_input_line, round_05, add_items


def main():

    shopping_basket = ShoppingBasket()

    while True:

        line_item = input("Enter: ")

        if line_item == 'y':
            break

        item = parse_input_line(line_item)

        add_items(shopping_basket, item)

    for item in shopping_basket.items:
        print(f'{item.quantity} {"imported" if item.imported else ""} {item.name}: {round(item.total_price, 2)}')
    print(f'Sales taxes: {round_05(shopping_basket.sales_taxes):.2f}')
    print(f'Total: {round(shopping_basket.total, 2):.2f}')


if __name__ == '__main__':
    main()
