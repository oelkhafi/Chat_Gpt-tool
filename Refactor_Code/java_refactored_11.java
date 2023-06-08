public static ArrayList<Integer> get_factors(int n) {
    if (n == 1) {
        return new ArrayList<Integer>();
    }
    int max = (int)(Math.sqrt(n) + 1.0);
    for (int