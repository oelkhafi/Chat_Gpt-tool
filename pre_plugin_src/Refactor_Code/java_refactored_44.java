public static ArrayList<ArrayList> subsequences(int a, int b, int k) {
    if (k == 0) {
        return new ArrayList();
    }

    ArrayList ret = new ArrayList(50);
    for (int i=a; i<