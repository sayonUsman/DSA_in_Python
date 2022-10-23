class Node:
	def __init__(self, data = None, link = None):
		self.data = data
		self.link = link
	
	
class LinkedList:
	def __init__(self):
		self.__head = None

	#FUNCTION START		
	def insert_at_beginning(self, data):
		node = Node(data = data, link = self.__head)
		self.__head = node
	#FUNCTION END

	#FUNCTION START		
	def insert_at_end(self, data):
		node = Node(data = data, link = None)
		
		if self.__head is None:
			self.__head = node
					
		else:
			temp_node  = self.__head
			
			while temp_node.link is not None:
				temp_node = temp_node.link
				
			temp_node.link = node
	#FUNCTION END

	#FUNCTION START		
	def remove(self, index):
		if self.__head is None:
			print("The Linked List is Empty.\n")
			return False
			
		elif index >= self.length():
			print("Please enter VALID INDEX NUMBER.\n")
			return None
				
		elif index == 0:
			temp_node = self.__head.link
			self.__head = temp_node
				
		elif index == self.length() - 1:
			temp_node  = self.__head	
			index2 = 0	
			
			while index2 < self.length() - 2:		
				temp_node = temp_node.link
				index2 += 1
				
			temp_node.link = None
			
		return True				
	#FUNCTION END

	#FUNCTION START						
	def print(self):	
		if self.__head is None:
			print("The Linked List is Empty.\n")
					
		else:
			temp_node  = self.__head
			print()
			
			while temp_node is not None:				
				if temp_node.link is None:
					print(f'{temp_node.data}\n')
					
				else:
					print(f'{temp_node.data}', end = " -> ")
					
				temp_node = temp_node.link
	#FUNCTION END

	#FUNCTION START			
	def length(self):
		if self.__head is None:
			return 0
					
		else:
			temp_node  = self.__head
			count = 0
			
		while temp_node is not None:
			count += 1
			temp_node = temp_node.link
							
		return count
	#FUNCTION END
				
				
if __name__ == '__main__':
	linked_list = LinkedList()
	
	while True:
		print('1. Insert at begining.')
		print('2. Insert at end.')
		print('3. Remove node.')
		print('4. Print the Linked List.')
		print('5. Print the length of the Linked List.')
		print('6. Exit.')
		
		try:
			choice = int(input("\nPlease enter your selected choice: "))
			
			if choice == 1:
				try:
					element = int(input(" \nPlease enter the element: "))
					linked_list.insert_at_beginning(element)
					print(f'{element} is added at the beginning of the Linked List Successfully.\n')			
					
				except Exception as Error:
					print(Error)
					print("Try again with INTEGER NUMBER.\n")
					
			elif choice == 2:
				try:
					element = int(input(" \nPlease enter the element: "))
					linked_list.insert_at_end(element)
					print(f'{element} is added at the end of the Linked List Successfully.\n')			
					
				except Exception as Error:
					print(Error)
					print("Try again with INTEGER NUMBER.\n")
					
			elif choice == 3:
				try:
					index = int(input('\nPlease enter the index number of node: '))
					is_deleted = linked_list.remove(index)
					
					if is_deleted:
						print("The node is deleted from Linked List Successfully.\n")		
					
				except Exception as Error:
					print(Error)
					print("Try again with INTEGER NUMBER.\n")	
					
			elif choice == 4:
				linked_list.print()
				
			elif choice == 5:
				length = linked_list.length()
				print(f"The length of the Linked List is {length}.\n")
				
			elif choice == 6:
				print("\nThe Linked Link have closed Successfully.")
				exit()
				
			else:
				print("\nPlease try with VALID NUMBER only.\n")
		
		except Exception as Error:
			print(Error)
			print("Please try again with VALID INPUT.\n")
							
