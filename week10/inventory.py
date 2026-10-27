# I thought list would be a really long complicated mumbo jumbo of words. Instead, I learned that its used to make things look cleaner within your code along with its normal use.
# A python list could be used to track sales, it would save time by automatically calculating totals and averages



# Exercise 1: Build a list

print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #always grabs the first item
print(inventory[-1]) #alway grabs the last item

middle = len(inventory) //2
print(inventory[middle]) #always grabs the middle item (no hard code)

# Exercise 3: List Slicing

print(" --- Exercise 3: List Slicing ---")
print(inventory[:3]) #grabs the first 3
print(inventory[-2:]) #grabs the last 2
print(inventory[::2]) 

# Exercise 4: List methods

print("--- Exercise 4: List methods ---")

inventory.append("envelope") # adds to the end of the list
print(inventory)

inventory.remove("tape") #perm removes something
print(inventory)

inventory.sort() #sorts in alphabetical order
print(inventory)

# Exercise 5: Tuple Comparison

print("--- Exercise 5: Tuple Comparison ---")
coords = [40.7128, -74.0060] # NYC cords

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")


# Exercise 6: List Average Sales

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sales: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f" Worst sale (loop): {worst}")

# Exercise 7: Accumulator pattern

print("--- Exercise 7: Accumulator pattern---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted= [] #empty list, so it can be used to append stuff to it
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales= []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")