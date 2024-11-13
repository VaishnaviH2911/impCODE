def fraction_knapsack():
    # Taking user inputs
    n = int(input("Enter the number of items: "))
    
    # Initializing empty lists for weights and values
    weights = []
    values = []
    
    # Input weights and values for each item
    for i in range(n):
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        value = float(input(f"Enter the value of item {i + 1}: "))
        weights.append(weight)
        values.append(value)
    
    # Input the capacity of the knapsack
    capacity = float(input("Enter the capacity of the knapsack: "))
    
    # Initialize the result (total profit)
    res = 0

    # Sorting the items by their value-to-weight ratio in descending order
    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:
            break

        # If the current item's weight is greater than the remaining capacity, take the fraction
        if pair[0] > capacity:
            res += int(capacity * (pair[1] / pair[0]))  # Add fractional value
            capacity = 0  # Knapsack is full

        # If the current item fits completely into the knapsack
        elif pair[0] <= capacity:
            res += pair[1]  # Add full value of the item
            capacity -= pair[0]  # Decrease the remaining capacity

        # Printing the current total profit after considering each item
        print(f"Current total profit: {res}")

    # Final total profit
    print(f"Maximum profit that can be obtained: {res}")

# Driver code to run the function
if __name__ == "__main__":
    fraction_knapsack()
