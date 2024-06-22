# Constants
PRICE_PER_LOAF = 185
DISCOUNT_RATE = 0.60

# Input: Number of day-old loaves being purchased
num_loaves = int(input("Enter the number of day-old bread loaves being purchased: "))

# Calculations
regular_price = num_loaves * PRICE_PER_LOAF
discount = regular_price * DISCOUNT_RATE
total_price = regular_price - discount

# Output: Displaying the prices with aligned decimal points
print(f"Regular price:  {regular_price:8.2f} rupees")
print(f"Discount:       {discount:8.2f} rupees")
print(f"Total price:    {total_price:8.2f} rupees")
