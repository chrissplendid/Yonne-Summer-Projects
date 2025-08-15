"""
Pizza Price Calculator
Author: Senior Software Engineer
Description: Calculates the total price of a pizza order 
             based on size, toppings, and extra cheese.
"""

# Constants (Global)
BASE_PRICES = {
    "small": 8.00,
    "medium": 10.00,
    "large": 12.00
}

TOPPING_PRICE = 1.50
EXTRA_CHEESE_PRICE = 2.00


def get_pizza_base_price(size: str) -> float:
    """
    Returns the base price of the pizza depending on the size.
    :param size: Pizza size ('small', 'medium', 'large')
    :return: Base price as float
    """
    return BASE_PRICES.get(size.lower(), 0.00)


def calculate_topping_cost(num_toppings: int) -> float:
    """
    Calculates the cost of additional toppings.
    :param num_toppings: Number of toppings
    :return: Total topping cost as float
    """
    return num_toppings * TOPPING_PRICE


def calculate_total_price(size: str, num_toppings: int, extra_cheese: bool) -> float:
    """
    Calculates the total price of the pizza order.
    :param size: Pizza size
    :param num_toppings: Number of toppings
    :param extra_cheese: True if extra cheese is added
    :return: Total price as float
    """
    base_price = get_pizza_base_price(size)
    toppings_cost = calculate_topping_cost(num_toppings)
    cheese_cost = EXTRA_CHEESE_PRICE if extra_cheese else 0.00
    
    return base_price + toppings_cost + cheese_cost


def main():
    """Main program function."""
    print("=== Welcome to the Pizza Price Calculator ===")
    
    size = input("Enter pizza size (small/medium/large): ").strip()
    num_toppings = int(input("Enter number of extra toppings: "))
    extra_cheese_input = input("Extra cheese? (yes/no): ").strip().lower()
    extra_cheese = (extra_cheese_input == "yes")
    
    total_price = calculate_total_price(size, num_toppings, extra_cheese)
    
    if total_price == 0:
        print("Invalid pizza size entered.")
    else:
        print(f"\nYour total pizza price is: ${total_price:.2f}")


if __name__ == "__main__":
    main()
