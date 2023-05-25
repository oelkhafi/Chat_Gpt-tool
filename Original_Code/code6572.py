from collections import Counter

class Node:
	def __init__(self, freq=0, letter="""", code="""", leaf=False):
		self.letter = letter
		self.freq = freq
		self.code = code
		self.is_leaf = leaf

	def left_right(self, left, right):
		self.left = left
		self.right = right

def tree_walk(node, res):
	if node.is_leaf == True:
		res[node.letter] = node.code
	else:
		node.left.code = node.code + ""0""		
		node.right.code = node.code + ""1""
		tree_walk(node.left, res)
		tree_walk(node.right, res)


def main():
	message = input()
	nodes = []
	for key,val in Counter(message).items():
		nodes.append(Node(letter=key, freq=int(val), leaf=True, code=""0""))


	nodes.sort(key = lambda x: -x.freq)
	while len(nodes) > 1:
		node_right = nodes.pop()
		node_left = nodes.pop()
		new_node = Node(freq = node_left.freq + node_right.freq)
		new_node.left_right(node_left, node_right)
		nodes.append(new_node)
		nodes.sort(key = lambda x: -x.freq)

	codebook = dict()
	tree_walk(nodes[0], codebook)

	encoded_message = """"
	for letter in message:
		encoded_message += codebook[letter]

	print(len(codebook), len(encoded_message))
	for key,val in codebook.items():
		print(f""{key}: {val}"")
	print(encoded_message)




if __name__ == ""__main__"":
	main()
 