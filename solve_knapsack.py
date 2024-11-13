def solve_knapsack():
    val = [50,100,150,200]
    wt = [8,16,32,40]
    w = 64
    n = len(val)-1
    def knapsack(w,n):
        if n < 0 or w <= 0:
            return 0
        
        if wt[n] > w:
            return knapsack(w,n-1)
        
        else:
            return max(val[n]+knapsack(w-wt[n],n-1),knapsack(w,n-1))
    print (knapsack(w,n))

if __name__ == "__main__":
    solve_knapsack()