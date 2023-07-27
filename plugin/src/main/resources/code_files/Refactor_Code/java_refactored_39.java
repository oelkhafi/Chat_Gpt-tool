public static int shortest_path_length(Map<List<Node>, Integer> length_by_edge, Node startnode, Node goalnode) {
    int n = length_by_edge.size();
    Map<Node, Integer> unvisitedNodes = new HashMap