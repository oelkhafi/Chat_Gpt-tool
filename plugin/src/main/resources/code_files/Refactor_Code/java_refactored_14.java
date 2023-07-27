public static ArrayList<Integer> kheapsort(ArrayList<Integer> arr, int k) {
    PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
    for (Integer v : arr.subList(0,k)) {
        heap.add(v