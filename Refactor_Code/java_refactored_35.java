public static ArrayList<Integer> quicksort(ArrayList<Integer> arr) {
    if (arr.isEmpty()) {
        return new ArrayList<Integer>();
    }

    Integer pivot = arr.get(0);
    ArrayList<Integer> lesser = new