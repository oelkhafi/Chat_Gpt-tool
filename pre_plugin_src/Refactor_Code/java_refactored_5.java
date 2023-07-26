public static boolean depth_first_search(Node startnode, Node goalnode) {
    Set<Node> nodesvisited = new HashSet<>();
    return search(startnode, goalnode, nodesvisited);
}

private static boolean search(Node node, Node goal