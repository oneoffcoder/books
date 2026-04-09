def calculate_total(price, quantity, tax_rate=0.0):
    """
    Calculate the final total for a purchase.

    Parameters:
        price: The price of one item.
        quantity: The number of items purchased.
        tax_rate: The tax rate as a decimal value.

    Returns:
        The final price after tax.
    """
    subtotal = price * quantity
    return subtotal * (1 + tax_rate)


print(calculate_total(10.0, 3, 0.07))
