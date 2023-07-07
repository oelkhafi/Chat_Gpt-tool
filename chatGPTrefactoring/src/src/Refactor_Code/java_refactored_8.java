public static int binsearch(int[] arr, int x, int start, int end) {
    if (start == end) {
        return -1;
    }
    int mid = start + (end - start) / 2;
    if (x < arr[mid])