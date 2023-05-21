def fractional_knapsack(capacity, weights, values):
    # Calculate value-to-weight ratio for each item
    ratios = [(values[i] / weights[i], weights[i]) for i in range(len(weights))]

    # Sort the items based on their value-to-weight ratio in descending order
    ratios.sort(reverse=True)

    total_value = 0  # Total value of selected items
    selected_items = []  # List to store selected items and their fractions

    for ratio, weight in ratios:
        if capacity == 0:
            break

        # Take the whole item if it can fit entirely in the knapsack
        if weight <= capacity:
            selected_items.append((1, weight))
            total_value += ratio * weight
            capacity -= weight
        else:
            # Otherwise, take a fraction of the item
            fraction = capacity / weight
            selected_items.append((fraction, capacity))
            total_value += ratio * capacity
            capacity = 0

    return total_value, selected_items


# Example usage
knapsack_capacity = 50
item_weights = [10, 20, 30]
item_values = [60, 100, 120]

max_value, selected_items = fractional_knapsack(knapsack_capacity, item_weights, item_values)

print("Selected items:")
for fraction, weight in selected_items:
    print(f"Fraction: {fraction}, Weight: {weight}")

print("Maximum value:", max_value)
