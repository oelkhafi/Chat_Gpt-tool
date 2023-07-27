public static int knapsack(int capacity, int [][] items) {
    int n = items.length;
    int memo[][] = new int[n + 1][capacity + 1];

    for (int i = 0; i <= n ; i++) {