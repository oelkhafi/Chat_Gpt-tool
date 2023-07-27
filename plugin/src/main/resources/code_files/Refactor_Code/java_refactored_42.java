public static boolean all(ArrayList<Boolean> arr) {
    return arr.stream().allMatch(Boolean::booleanValue);
}

public static boolean any(ArrayList<Boolean> arr) {
    return arr.stream().anyMatch(Boolean::bo