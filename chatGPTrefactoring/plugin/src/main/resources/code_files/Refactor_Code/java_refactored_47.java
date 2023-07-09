public static ArrayList<String> wrap(String text, int cols) {
    ArrayList<String> lines = new ArrayList<>();
    while (text.length() > cols) {
        int end = text.lastIndexOf(" ", cols);
        if