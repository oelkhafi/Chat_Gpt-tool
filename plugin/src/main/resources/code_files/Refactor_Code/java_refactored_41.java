public static List shunting_yard(ArrayList tokens) {
    Map<String, Integer> precedence = new HashMap<>();
    precedence.put("+",1);
    precedence.put("-",1);
    precedence.put("*",2);
    precedence.