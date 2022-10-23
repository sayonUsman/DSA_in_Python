from collections import deque

class Stack:
	def __init__(self):
		self.__stack = deque([])
		
	def append(self, item):
		self.__stack.append(item)
		
	def length(self):
		return len(self.__stack)
		
	def pop(self):
		if len(self.__stack) == 0:
			return None
			
		else:
			return self.__stack.pop()
	
	def print(self):
		if len(self.__stack) == 0:
			print("The stack is empty.\n")
			
		else:
			print()
			
			for item in self.__stack:
				print(item)
	
			print()
		
	
stack = Stack()

while True:
		print("1. Add the item in the stack.")
		print("2. Delete the item in the stack.")
		print("3. Print the items of the stack.")
		print("4. Print the length of the stack.")
		print("5. Exit.")
		
		try:
			choice = int(input("\nPlease enter your selected choice: "))
			
			if choice == 1:
				try:
					element = int(input(" \nPlease enter the item: "))
					stack.append(element)
					print(f'{element} is added at the end of the stack successfully.\n')			
					
				except Exception as Error:
					print(Error)
					print("Try again with INTEGER NUMBER.\n")
					
			elif choice == 2:
				element = stack.pop()
				
				if element is None:
					print("The stack is empty.\n")
				
				else:	
					print(f'{element} is removed from the end of the stack successfully.\n')			
					
			elif choice == 3:
				stack.print()
				
			elif choice == 4:
				length = stack.length()
				print(f"The number of items in the stack is {length}.\n")
				
			elif choice == 5:
				print("\nThe stack have closed successfully.")
				exit()
				
			else:
				print("\nPlease try with VALID NUMBER only.\n")
		
		except Exception as Error:
			print(Error)
			print("Please try again with VALID INPUT.\n")
		