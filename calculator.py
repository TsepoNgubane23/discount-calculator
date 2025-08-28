
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise return original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price


# --- Program Execution ---
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after discount: {final_price}")
    else:
        print(f"No discount applied. Final price: {final_price}")

except ValueError:
    print("⚠️ Please enter valid numeric values for price and discount.")
