import sys
from collections import namedtuple


Node = namedtuple(""Node"", [""page_rank"", ""adjacency_list""])


def _emit(nid, value):
    if isinstance(value, Node):
        adjacency_list = ""{"" + "","".join(map(str, value.adjacency_list)) + ""}""
        page_rank = value.page_rank
    else:
        adjacency_list = ""{}""
        page_rank = value

    print(f""{nid}\t{round(page_rank, 3)}\t{adjacency_list}"")


def _map(nid, node):
    _emit(nid, node)

    p = node.page_rank / len(node.adjacency_list)
    for adjacency_nid in node.adjacency_list:
        _emit(adjacency_nid, p)


def main():
    for line in sys.stdin:
        nid, page_rank, adjacency_list = line.rstrip().split(""\t"")
        nid = int(nid)
        node = Node(float(page_rank), tuple(map(int, adjacency_list.strip(""{}"").split("",""))))

        _map(nid, node)


if __name__ == ""__main__"":
    main() 