public static int levenshtein(String source, String target) {
    if (source.equals("")) {
        return target.length();
    } else if (target.equals("")) {
        return source.length();
    } else {
        int cost =