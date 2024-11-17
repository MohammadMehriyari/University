
class newNode:

	#create a new node
	def __init__(self, data):
		self.data = data
		self.next = None

# insert a node at the beginning of the linked list
def push(node,data):
	if (node == None):
		return (newNode(data))
	else:
		node.next = push(node.next, data)
		return node

# find the avg of nodes of the given linked list
def avgOfNodes(head):
	if (head == None):
		return -1
	
	count = 0 
	sum = 0
	avg = 0.0

	while (head != None):
		count += 1
		sum += head.data
		head = head.next
	
	avg = sum / count
	return avg

# create linked list 9.2.2.7.5
head = newNode(9)
push(head, 2)
push(head, 2)
push(head, 7)
push(head, 5)
print("Average of nodes = ",avgOfNodes(head))

