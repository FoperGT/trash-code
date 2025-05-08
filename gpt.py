from typing import List, Dict, Tuple


def calculate_statistics(items: List[Dict]) -> Tuple[float, float, List[str], List[str]]:
    total_cost = 0
    total_quantity = 0
    unique_items = set()
    max_price = 0
    most_expensive_items = set()

    for item in items:
        name = item['name']
        price = item['price']
        quantity = item['quantity']

        total_cost += price * quantity
        total_quantity += quantity
        unique_items.add(name)

        if price > max_price:
            max_price = price
            most_expensive_items = {name}
        elif price == max_price:
            most_expensive_items.add(name)

    average_price = total_cost / total_quantity if total_quantity else 0

    return total_cost, average_price, list(unique_items), list(most_expensive_items)


def print_statistics(total: float, average: float, unique: List[str], expensive: List[str]) -> None:
    print(f"Total cost: {total:.2f}")
    print(f"Average item price: {average:.2f}")
    print(f"Unique items: {', '.join(sorted(unique))}")
    print(f"Most expensive items: {', '.join(sorted(expensive))}")


if __name__ == "__main__":
    purchases = [
        {'name': 'apple', 'price': 2, 'quantity': 5},
        {'name': 'banana', 'price': 1, 'quantity': 10},
        {'name': 'apple', 'price': 2, 'quantity': 3},
        {'name': 'orange', 'price': 3, 'quantity': 2},
        {'name': 'banana', 'price': 1, 'quantity': 4},
        {'name': 'kiwi', 'price': 5, 'quantity': 1}
    ]

    total, average, unique_items, most_expensive = calculate_statistics(purchases)
    print_statistics(total, average, unique_items, most_expensive)
