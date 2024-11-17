# Node class
class Node:

	# initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	#  initialize head
	def __init__(self):
		self.head = None

	# insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# print the LinkedList
	def printList(self):
		temp = self.head
		print(temp.data,end=' ')
		temp = temp.next
		while(temp != self.head):
			print (temp.data,end=' ')
			temp = temp.next

	# Algorithm 
	def sortedInsert(self, new_node):
		
		current = self.head
		
		if current is None:
			new_node.next = new_node
			self.head = new_node
		
		elif (current.data >= new_node.data):
			
			# If value is smaller than head's value then we need to change next of last node
			while current.next != self.head :
				current = current.next
			current.next = new_node
			new_node.next = self.head
			self.head = new_node			

		
		else:
			
			# Locate the node before the point of insertion
			while (current.next != self.head and
				current.next.data < new_node.data):
				current = current.next

			new_node.next = current.next
			current.next = new_node


arr = [7, 16, 2, 2, 23, 70]

list_size = len(arr)

# empty linked list
start = LinkedList()

# Create linked list from the array arr[]
for i in range(list_size):
	temp = Node(arr[i])
	start.sortedInsert(temp)

start.printList()

