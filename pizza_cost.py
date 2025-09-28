#!/usr/bin/env python3
# Created by: Shem
# Created on: 9/27/2025
# This calculates and displays the input and the order type of a pizza

import constant


def main():
    # This is to take the input of the order
    diameter = int(
        input("Choose from the selection Large = 18, Medium = 16, Small = 12: ")
    )

    # This does the subtotal
    subtotal = (
        constant.LABOUR_COST
        + constant.RENTAL_COST
        + constant.INGREDIENT_COST * diameter
    )

    # Plus tax
    tax = constant.HST * subtotal

    # And total
    total = subtotal + tax

    # Output
    print("")
    print("The subtotal cost is = ${:,.2f}".format(subtotal))
    print("pluse tax is  = ${:,.2f}".format(tax))
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
