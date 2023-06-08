public static int find_first_in_sorted(int[] arr, int x) {
    int lo = 0;
    int hi = arr.length;

    while (lo <= hi) {
        int mid = (lo + hi) / 2;

        if (x