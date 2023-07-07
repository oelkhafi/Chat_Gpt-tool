public static Set<WeightedEdge> minimum_spanning_tree(List<WeightedEdge> weightedEdges) {
    Map<Node,Set<Node>> groupByNode = new HashMap<>();
    Set<WeightedEdge> minSpanningTree = new HashSet