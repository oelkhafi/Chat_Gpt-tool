class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

class Huffman_Tree (Tree):
 
    def new_key(self, sym, bitcode):
        pointer = self
        for bit in bitcode:
            if bit == '0':
                if pointer.left is None:
                    pointer.left = Tree()
                pointer = pointer.left
            else:
                if pointer.right is None:
                    pointer.right = Tree()
                pointer = pointer.right
        pointer.data = sym

    def decode(self, bitseq):
        result = []
        pointer = self
        for bit in bitseq:
            pointer = (pointer.left, pointer.right)[bit == '1']
            if pointer.data is not None:
                result.append(pointer.data)
                pointer = self
        return ''.join(result)

def Huffman_decode(coded: str, d: dict) -> str:
    root = Huffman_Tree()
    for sym, code in d.items():
        root.new_key(sym, code)
    return root.decode(coded)


difsyms, codelen = map(int, input().split())
code_table = dict(input().split(': ') for _ in range(difsyms))
to_decode = input()
print(Huffman_decode(to_decode, code_table))
 