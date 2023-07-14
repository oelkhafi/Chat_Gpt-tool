public static ArrayList<Integer> bucketsort(ArrayList<Integer> arr, int k) {
    ArrayList<Integer> counts = new ArrayList<>(Collections.nCopies(k, 0));
    for (Integer x : arr) {
        counts.set(x