public static ArrayList<Integer> next_permutation(ArrayList<Integer> perm) {
    for (int i=perm.size()-2; i!=-1; i--) {
        if (perm.get(i) < perm.get(i+1)) {