public static boolean detect_cycle(Node node) {
    Node hare = node;
    Node tortoise = node;

    while (true) {
        if (hare.getSuccessor() == null)
            return false;

        tortoise = tortoise.getSuccessor