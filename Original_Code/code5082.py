import sys
from collections import namedtuple


Node = namedtuple(""Node"", [""page_rank"", ""adjacency_list""])
ALPHA = 0.1
N = 5


def _emit(nid, node):
    adjacency_list = ""{"" + "","".join(map(str, node.adjacency_list)) + ""}""
    page_rank = node.page_rank

    print(f""{nid}\t{round(page_rank, 3)}\t{adjacency_list}"")


def _reduce(nodes):
    for nid, node_list in nodes.items():
        structural_node = None
        page_rank = 0
        for node in node_list:
            if node.adjacency_list:
                structural_node = node
            else:
                page_rank += node.page_rank

        page_rank = ALPHA * (1/N) + (1 - ALPHA) * page_rank
        _emit(nid, Node(page_rank, structural_node.adjacency_list))


def main():
    nodes = {}
    for line in sys.stdin:
        nid, page_rank, adjacency_list = line.rstrip().split(""\t"")
        nid = int(nid)
        if len(adjacency_list) > 2:
            adjacency_list = tuple(map(int, adjacency_list.strip(""{}"").split("","")))
        else:
            adjacency_list = tuple()
        node = Node(float(page_rank), adjacency_list)

        nodes.setdefault(nid, []).append(node)

    _reduce(nodes)


if __name__ == ""__main__"":
    main() 