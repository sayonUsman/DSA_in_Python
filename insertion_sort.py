class InsertionSort:
	def __init__(self, list):
		self.list = list
		
	def insertion_sort(self):
		for index in range(1, len(self.list)):
			current = self.list[index]
			index2 = index - 1
			while index2 >= 0 and self.list[index2] > current:
				self.list[index2 + 1] = self.list[index2]
				index2 -= 1			
			self.list[index2 + 1] = current 


numbers = list(map(int, input("Please enter the list of number: ").split()))
insertionSort = InsertionSort(numbers)
insertionSort.insertion_sort()
print(numbers)
