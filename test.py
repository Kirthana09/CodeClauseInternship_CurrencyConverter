from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    """
    Converts amount from one currency to another.

    Args:
        amount (float): The amount to be converted.
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.

    Returns:
        float: The converted amount.
    """
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

if __name__ == "__main__":
    # Input currency details
    amount = float(input("Enter the amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()

    # Convert currency
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} equals {converted_amount} {to_currency}")

