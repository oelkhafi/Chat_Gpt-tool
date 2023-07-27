public int compareTo(WeightedEdge compareNode) {
    int compareWeight= compareNode.weight;
    return this.weight - compareWeight;
}