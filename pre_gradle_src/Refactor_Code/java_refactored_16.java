public static Integer kth(ArrayList<Integer> arr, int k) {
    int pivot = arr.get(0);
    ArrayList<Integer> below = new ArrayList<Integer>(arr.size());
    ArrayList<Integer> above = new ArrayList<Integer>(arr