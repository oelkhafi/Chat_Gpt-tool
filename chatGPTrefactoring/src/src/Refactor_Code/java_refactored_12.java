public static List<Pair<Integer,Integer>> hanoi(int height, int start, int end) {
    ArrayList<Pair<Integer,Integer>> steps = new ArrayList<Pair<Integer,Integer>>();
    if (height > 0) {
        int