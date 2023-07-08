public static Double rpn_eval(ArrayList tokens) {
    Map<String, BinaryOperator<Double>> op = new HashMap<>();
    op.put("+", (a, b) -> a + b);
    op.put("-", (a, b