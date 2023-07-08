public static ArrayList<Node> topological_ordering(List<Node> directedGraph) {
    ArrayList<Node> orderedNodes = new ArrayList<Node>();
    for (Node node : directedGraph) {
        if (node.getPredecessors().isEmpty())