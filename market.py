# Assignment blues part 1

# Part 1

# Create a dictionary to store my list of items, with price and stock

# produce = {

    # "beets": {
        # "price": 1500,
        # "stock": 60
    
    # "arugula": {
        # "price": 1200,
        # "stock": 30
    
    # "spinach": {
        # "price": 500,
        # "stock": 100
    
    # "apples": {
        # "price": 1000,
        # "stock": 100
    
    # "okra": {
        # "price": 2500,
        # "stock": 40
    
    # "pomegranates": {
        # "price": 3000,
        # "stock": 100
    
    # "figs": {
        # "price": 2000,
        # "stock": 100
    

# Create a shopping list of the items above

# shopping_list = ["beets", "arugula", "spinach", "spinach", "apples", "okra", "pomegranates", "okra"]

# Dictionary to track purchased items for the bill

# purchased_items = {}

# Initialising the total cost variable

# total_cost = 0

# Adding control flow to process the shopping list - Part 2
# Another attempt at the for loop

# for item in shopping_list: # Check for availability of the item
    # if item in produce: # Check for stock quantities
        # if stock[item] > 0:
            # total_cost = total_cost + produce[item] 

    # Reduce stock items

    # stock[item] = stock[item] - 1

        # else:  
            # print(f"{item} is out of stock!")

    # else: # When item is not in my list
        # print(f"{item} not found in inventory!")

    # print(f"Final Total Cost:" {total_cost})
    # print("Remaining Stock:", stock)
        
# Calculate and return final bill

# print("\n" +"="*30)
# print("       Final Bill is")
# print("="*30)

# Return each purchased item, its quantity and line total

# for item in purchased_items:

    # quantity = purchased_items[item]  # Get the quantity value

    # price_per_item = produce[item]  # Get the price of one item

    # line_price = price_per_item * quantity  # Calculate the total line item

    # print(f"- {item.capitalize()}(x{quantity}: {line_total} UShs)")  # This line I had to google :) 

# print("="*30)

# Print totals

# print(f"Grand total:     {total_cost}  UShs")
# print("="*30)
# print("Thank you for your purchase!")
            
# Part 3 - with reusable functions and return results like walked through above - not adding comments to explain


produce = {

    "beets": {
        "price": 1500,
        "stock": 60
    },
    "arugula": {
        "price": 1200,
        "stock": 30
    },
    "spinach": {
        "price": 500,
        "stock": 100
    },
    "apples": {
        "price": 1000,
        "stock": 100
    },
    "okra": {
        "price": 2500,
        "stock": 40
    },
    "pomegranates": {
        "price": 3000,
        "stock": 100
    },
    "figs": {
        "price": 2000,
        "stock": 100
    }
}

shopping_list = ["beets", "arugula", "spinach", "spinach", "apples", "okra", "pomegranates", "okra"]


def calculate_bill(inventory, customer_list):
    """
    Processes a customer's shopping list against the store's inventory,
    then calculates and prints the final bill.
    """
    total_cost = 0
    purchased_items = {}

    print("Processing your shopping list....")

    for item in customer_list:
        if item in inventory:
            if inventory[item]["stock"] > 0:
                price = inventory[item]["price"]
                total_cost += price
                inventory[item]["stock"] -= 1

                if item in purchased_items:
                    purchased_items[item] += 1
                else:
                    purchased_items[item] = 1
            else:
                print(f"Note: {item} is out of stock!")
        else:
            print(f"Note: {item} is not sold here!")

    print("\n" + "=" * 30)
    print("       Final Bill is")
    print("=" * 30)

    for item, quantity in purchased_items.items():
        line_total = inventory[item]["price"] * quantity
        print(f"- {item.capitalize()} (x{quantity}): {line_total} UShs")

    print("=" * 30)
    print(f"Grand Total: {total_cost} UShs")
    print("-" * 30)

# Run the function
calculate_bill(produce, shopping_list)




