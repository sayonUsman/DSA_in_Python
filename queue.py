from collections import deque

class Queue:
	def __init__(self):
		self.__queue = deque([])
		
	def append(self, item):
		self.__queue.append(item)
		
	def length(self):
		return len(self.__queue)
		
	def pop(self):
		if len(self.__queue) == 0:
			return None
		
		else:
			return self.__queue.popleft()
	
	def print(self):
		if len(self.__queue) == 0:
			print("The queue is empty.\n")
			
		else:
			print()
			
			for item in self.__queue:
				print(item)
				
			print()
		
	
queue = Queue()

while True:
		print("1. Add the item in the queue.")
		print("2. Delete the item in the queue.")
		print("3. Print the items of the queue.")
		print("4. Print the length of the queue.")
		print("5. Exit.")
		
		try:
			choice = int(input("\nPlease enter your selected choice: "))
			
			if choice == 1:
				try:
					element = int(input(" \nPlease enter the item: "))
					queue.append(element)
					print(f'{element} is added at the end of the queue successfully.\n')			
					
				except Exception as Error:
					print(Error)
					print("Try again with INTEGER NUMBER.\n")
					
			elif choice == 2:
				element = queue.pop()
				
				if element is None:
					print("The queue is empty.\n")
					
				else:
					print(f'{element} is removed from the beginning of the queue successfully.\n')			
					
			elif choice == 3:
				queue.print()
				
			elif choice == 4:
				length = queue.length()
				print(f"The number of items in the queue is {length}.\n")
				
			elif choice == 5:
				print("\nThe queue have closed successfully.")
				exit()
				
			else:
				print("\nPlease try with VALID NUMBER only.\n")
		
		except Exception as Error:
			print(Error)
			print("Please try again with VALID INPUT.\n")
		