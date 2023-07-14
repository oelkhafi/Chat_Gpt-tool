public static int lis(int[] arr) {
    Map<Integer,Integer> ends = new HashMap<Integer, Integer>(100);
    int longest = 0;

    int i = 0;
    for (int val : arr) {

        ArrayList<Integer> prefix