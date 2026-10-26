# The first bug i spotted was the missin colon. I found it in the traceback and it told me which line it was in. I found it without using AI. I feel like I currently have only beginner debugging instincts because i couldn't find anything else without AI
# It takes the original price and the customers discount tier, which it then uses the tier to calculat the discount. it then returns the final price when the calculations are finished. A colleague could probably understand it without reading the body just because the names of the inputs are simple.
# I used AI twice trying to fix the broken sales.py, it really helped me understand what was wrong along with it explaining why its correct.

# Exercise 1

# Defining a function

def calculate_tax(price, rate):
    return price * rate

# callinf a function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: {tax1:.2f}")
print(f"Tax for $250 at 8%: {tax2}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2

# Defining a function to apply discount based on membership tier

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
# calling the function with different tiers
original_price = 200

for tier in["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Calling the final_price function\
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 6

x = 100 #global x

def double_it():
    x = 999 #local X
    return x * 2

print(x)
print(double_it())
print(x)

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #This needs the "+" because it makes it add the new value to the existing value, while just a "=" would replace the value of total with the current sale
print(f"Total: ${total}")

count = 0
for sale in sales: #need to add colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #need to remove "=" because it python allows the "i" to reach 5 even though it doesnt exist, so then it crashes
    print(sales[i])
    i += 1
