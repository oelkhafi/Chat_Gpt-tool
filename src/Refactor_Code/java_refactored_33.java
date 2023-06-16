public static ArrayList<ArrayList> powerset(ArrayList arr) {
    if (!arr.isEmpty()) {
        Object first = arr.get(0);
        arr.remove(0);
        ArrayList rest = arr;
        ArrayList<ArrayList> rest_