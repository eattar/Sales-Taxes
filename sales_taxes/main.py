from sales_taxes.shopping_basket import ShoppingBasket
from sales_taxes.item import parse_input_line
from sales_taxes.round_up_to_nearest_05 import roundup_nearest_05


def main():
    """prints out receipt details of a shopping basket"""
    shopping_basket = ShoppingBasket()

    print("\n[q] SHOW RESULTS")
    while True:

        line_item = input("Add Item: ")

        if line_item == 'q':
            break

        try:
            item = parse_input_line(line_item)
            shopping_basket.add_items(item)
        except Exception as error:
            print(error)
            continue

    print("\n")

    for item in shopping_basket.items:
        print(item)
    print(f'Sales Taxes: {roundup_nearest_05(shopping_basket.total_sales_taxes()):.2f}')
    print(f'Total: {round(shopping_basket.total_price(), 2):.2f}\n')


if __name__ == '__main__':
    main()
