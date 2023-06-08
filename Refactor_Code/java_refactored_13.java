public static Boolean is_valid_parenthesization(String parens) {
    int depth = 0;
    for (int i = 0; i < parens.length(); i++) {
        char paren = parens.charAt(i);
        if (