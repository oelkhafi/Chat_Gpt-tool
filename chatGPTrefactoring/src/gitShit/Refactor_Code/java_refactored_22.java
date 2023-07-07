public static int max_sublist_sum(int[] arr) {
    int max_ending_here = 0;
    int max_so_far = 0;

    for (int x : arr) {
        max_ending_here = Math.max(x, max_