inventory = [
    {"name": "apples", "quantity": 2},
    {"name": "bananas", "quantity": 0},
    {"name": "cherries", "quantity": 5},
    {"name": "oranges", "quantity": 10},
    {"name": "berries", "quantity": 7},
]

def checkIfFruitPresent(foodlist: list, target: str):
    # Check if the name is present ins the list or not
    print(f"We keep {target} inventory") if target in list(
        map(lambda x: x["name"], foodlist)
    ) else print(f"We dont keep {target} at our store")


def checkIfFruitInStock(foodlist: list, target: str):
    # First check if the fruit is present in the list
    if target in list(map(lambda x: x["name"], foodlist)):
        # If fruit is present then check if the quantity of the fruit is greater than 0
        print(f"{target} is in stock") if list(
            filter(lambda fruit: fruit["name"] == target, foodlist)
        )[0]["quantity"] > 0 else print(f"{target} is out of stock")
    else:
        print(f"We dont keep {target} at our store")


checkIfFruitPresent(inventory, "apples")
checkIfFruitInStock(inventory, "apples")
checkIfFruitInStock(inventory, "bananas")
checkIfFruitInStock(inventory, "tomatoes")
