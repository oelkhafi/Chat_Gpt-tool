public static int levenshtein(String source, String target) {
    if (source.isEmpty() || target.isEmpty()) {
        return source.isEmpty() ? target.length() : source.length();
    } else if (source.charAt(0) ==