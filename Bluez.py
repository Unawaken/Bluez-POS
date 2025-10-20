# Console Program for Bluez Coffee Shop

# Coffee menu - prices in pesos (₱)
# Global Dictionary
menu = {
    "Caramel Macchiato": 125.00,
    "Salted Caramel": 176.50,
    "Spanish Latte": 135.00,
    "Matcha": 110.12,
    "Pumpkin Spiced Latte": 142.59
}

# Inventory Dictionary
inventory = {
    "Coffee Beans (g)": 5000,
    "Milk (ml)": 10000,
    "Syrup (ml)": 3000,
    "Matcha Powder (g)": 1500,
    "Pumpkin Spice Syrup (ml)": 1000
}

# Ingredient Usage per Coffee
ingredient_usage = {
    "Caramel Macchiato": {"Coffee Beans (g)": 18, "Milk (ml)": 150, "Syrup (ml)": 30},
    "Salted Caramel": {"Coffee Beans (g)": 18, "Milk (ml)": 150, "Syrup (ml)": 40},
    "Spanish Latte": {"Coffee Beans (g)": 18, "Milk (ml)": 120},
    "Matcha": {"Matcha Powder (g)": 15, "Milk (ml)": 200},
    "Pumpkin Spiced Latte": {"Coffee Beans (g)": 18, "Milk (ml)": 150, "Pumpkin Spice Syrup (ml)": 30}
}


# Functions

# Display Menu Function
def display_menu():
    """Prints the current coffee menu with prices."""
    print("\n" + "="*35)
    print("      Bluez COFFEE MENU")
    print("="*35)

    # Use enumerate to display options starting from 1
    for index, (coffee, price) in enumerate(menu.items(), 1):
        print(f"({index}) {coffee:<20} ₱{price:.2f}")
    print("="*35)

# Display Inventory Function
def display_inventory():
    """Prints the current ingredient stock levels."""
    print("\n" + "="*40)
    print("        CURRENT INVENTORY STOCK")
    print("="*40)
    for ingredient, stock in inventory.items():
        print(f"{ingredient:<25} {stock}")
    print("="*40)

# Check Inventory Function
def check_inventory(coffee, quantity):
    """Checks if there's enough stock for the order."""
    if coffee not in ingredient_usage:
        return True, "No ingredient usage defined for this item."

    for ingredient, usage_per_cup in ingredient_usage[coffee].items():
        required = usage_per_cup * quantity
        if inventory.get(ingredient, 0) < required:
            return False, "Insufficient stock of {ingredient}. Need {required}, but only have {inventory.get(ingredient, 0)}."

    return True, "Stock is sufficient."

# Inventory Update Function
def update_inventory(coffee, quantity):
    """Deducts ingredients from inventory after a successful order."""
    if coffee not in ingredient_usage:
        return

    for ingredient, usage_per_cup in ingredient_usage[coffee].items():
        required = usage_per_cup * quantity
        # Deduct the required amount
        inventory[ingredient] -= required


# Getting the user's coffee choice function
def get_coffee_choice():
    """Gets the user's coffee choice based on menu index."""
    display_menu()

    while True:
        try:
            choice = int(input("Please select your coffee (1-5): "))
            if 1 <= choice <= 5:
                # Convert the user's number choice to the actual coffee name
                coffee_list = list(menu.keys())
                selected_coffee = coffee_list[choice - 1]
                return selected_coffee
            else:
                print("Invalid choice! Please select 1-5.")
        except ValueError:
            print("Please enter a valid number!")

# Specifying the quantity of the user's input
def get_quantity():
    """Gets the desired quantity of coffee cups."""
    while True:
        try:
            qty = int(input("How many cups would you like? "))
            if qty > 0:
                return qty
            else:
                print("Please enter a number greater than 0!")
        except ValueError:
             print("Please enter a valid number!")

# Caculates the total of the coffee price based on its quantity
def calculate_total(coffee, quantity):
    """Calculates the total price of the order."""
    coffee_price = menu.get(coffee, 0)
    total = coffee_price * quantity
    return coffee_price, total

# Ouputs the order summary
def display_order_summary(coffee, quantity, coffee_price, total):
    """Prints a summary of the order details."""
    print("\n" + "="*40)
    print("           ORDER SUMMARY")
    print("="*40)
    print(f"Coffee: {coffee.title()}")
    print(f"Coffee Price: ₱{coffee_price:.2f}")
    print(f"Quantity: {quantity}x")
    print("-"*40)
    print(f"TOTAL: ₱{total:.2f}")
    print("="*40)

# Virtual payment function
def get_payment(total):
    """Processes payment and calculates change."""
    print(f"\nTotal amount due: ₱{total:.2f}")

    current_payment = 0.0
    while True:
        try:
            needed = total - current_payment
            payment_input = float(input(f"Enter payment amount (₱{needed:.2f} remaining): ₱"))

            current_payment += payment_input
            if current_payment >= total: # Check the accumulated payment
                change = current_payment - total
                return current_payment, change # Return the accumulated payment
            else:
                # Use total
                print(f"Insufficient payment! You need ₱{total - current_payment:.2f} more.") # Use current_payment
        except ValueError:
            print("Please enter a valid amount!")

def print_receipt(coffee, quantity, coffee_price, total, payment, change):
    """Generates and prints the final sales receipt."""
    print("\n" + "="*50)
    print("                   RECEIPT")
    print("              Bluez COFFEE SHOP")
    print("="*50)

    #print(f"Date: Today")
    #print(f"Order #: 001")

    print("\nITEMS ORDERED:")
    print("-" * 30)
    print(f"{quantity}x {coffee.title():<20} ₱{coffee_price:.2f}")
    print("-" * 30)
    print(f"Subtotal: ₱{total:.2f}")
     # Placeholder
    print(f"TOTAL: ₱{total:.2f}")
    print(f"Payment: ₱{payment:.2f}")
    print(f"Change: ₱{change:.2f}")

    print("="*50)
    print("        THANK YOU FOR YOUR ORDER!")
    print("            ENJOY YOUR COFFEE!")
    print("="*50)


# MAIN EXECUTION FUNCTION


def main():
    """Main function to run the coffee shop program flow."""
    print("Starting Bluez POS....")
    # Display Current Program Status
    display_inventory()

    # Get Order Details
    coffee = get_coffee_choice()
    quantity = get_quantity()

    # Check Inventory before proceeding
    stock_ok, message = check_inventory(coffee, quantity)
    if not stock_ok:
        print(f"\nORDER CANCELLED: {message}")
        print("Please restock ingredients and try again.")
        return # Exit main function if stock is low

    # Calculate Pricing
    coffee_price, total = calculate_total(coffee, quantity)

    # Show Order Summary
    display_order_summary(coffee, quantity, coffee_price, total)

    # Confirm Order
    confirm = input("\nConfirm Order? (Y/n): ").lower()
    if confirm not in ['y', 'yes']:
        print("Order has been cancelled. Thank you!")
        return

    # Get Payment
    payment, change = get_payment(total)

    # Update Inventory
    update_inventory(coffee, quantity)
    print("\n*** Inventory updated successfully! ***")

    # Print Receipt
    print_receipt(coffee, quantity, coffee_price, total, payment, change)

    # Display Final Message
    print(f"\nOrder complete successfully! You ordered {quantity}x {coffee.title()}.")
    # Display inventory after order
    display_inventory()


# Run the program
if __name__ == "__main__":
    main()
