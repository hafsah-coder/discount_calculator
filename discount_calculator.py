def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount_percent is less than 20, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# --- Main Program ---
# Prompt the user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Get the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"The final price after applying a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")

