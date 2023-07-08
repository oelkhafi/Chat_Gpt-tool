public static boolean breadth_first_search(Node startnode, Node goalnode) {
    Deque<Node> queue = new ArrayDeque<>();
    queue.addLast(startnode);

    nodesvisited.add(startnode);

    while (!queue.is