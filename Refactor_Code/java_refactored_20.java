public static String longest_common_subsequence(String a, String b) {
    if (a.isEmpty() || b.isEmpty()) {
        return "";
    } else if (a.charAt(0) == b.charAt(0)) {
        return