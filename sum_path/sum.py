import karantools as kt

class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.value)

def make_nodes():
	current_nodes = []
	previous_nodes = []
	nodes_list = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
	for i in range(len(nodes_list) - 1, -1, -1):
		for k in range(len(nodes_list[i])):
			if previous_nodes != []:
				node = Node(nodes_list[i][k], previous_nodes[k], previous_nodes[k + 1])
			else:
				node = Node(nodes_list[i][k], None, None) 
			current_nodes.append(node)
		previous_nodes = current_nodes
		current_nodes = []
	return previous_nodes[0]

top_node = make_nodes()

def left_sum(limit):
	total = top_node.value
	current_node = top_node
	for j in range(limit):
		total += current_node.left.value
		current_node = current_node.left
	return total

def right_sum(limit):
	total = top_node.value
	current_node = top_node
	for j in range(limit):
		total += current_node.right.value
		current_node = current_node.right
	return total

def bfs(top_node):
	queue = [(top_node, 0)]
	total = 0
	while queue:
		s, pretotal = queue.pop(0)
		pretotal += s.value
		if s.left != None:
			queue.append((s.left, pretotal))
		if s.right != None:
			queue.append((s.right, pretotal))
		if s.left == None:
			if pretotal > total:
				total = pretotal 
	return total

def max_sum():
	nodes_list = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
	previous_sums = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
	current_sums = [] 
	for row in range(len(nodes_list) - 2, -1, -1):
		for node in range(row + 1):
			if previous_sums[node] > previous_sums[node + 1]:
				current_sums.append(nodes_list[row][node] + previous_sums[node])  
			else:
				current_sums.append(nodes_list[row][node] + previous_sums[node + 1])
		previous_sums = current_sums
		current_sums = []
	return previous_sums[0]


with kt.timer():
	for i in range(40000): 
		max_sum()

with kt.timer():
	for i in range(20):
		bfs(top_node)

print(max_sum())
print(bfs(top_node))

