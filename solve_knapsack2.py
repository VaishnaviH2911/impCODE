def solve_knapsack():
    # Take the number of items as input
    n = int(input("Enter the number of items: "))

    # Take values and weights as input
    val = []
    wt = []
    
    for i in range(n):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        val.append(value)
        wt.append(weight)

    # Take the capacity of the knapsack as input
    w = int(input("Enter the capacity of the knapsack: "))
    
    # Recursive knapsack function
    def knapsack(w, n):
        if n < 0 or w <= 0:  # Base case
            return 0
        
        if wt[n] > w:  # If the item cannot be included in the knapsack
            return knapsack(w, n-1)
        else:  # Otherwise, take the maximum of including or excluding the item
            return max(val[n] + knapsack(w - wt[n], n - 1), knapsack(w, n - 1))

    # Call the knapsack function and print the result
    print("Maximum value in knapsack =", knapsack(w, n-1))

if __name__ == "__main__":
    solve_knapsack()
