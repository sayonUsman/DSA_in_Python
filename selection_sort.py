class SelectionSort:
	def __init__(self, list):
		self.list = list
		
	def swap(self, index, index2):
		temp = self.list[index]
		self.list[index]= self.list[index2]
		self.list[index2] = temp
		
	def selection_sort(self):
		for index in range(len(self.list) - 1):
			min_index = index
			for index2 in range(index + 1, len(self.list)):
				if self.list[min_index] > self.list[index2]:
					min_index = index2
			self.swap(min_index, index)
					

numbers = list(map(int, input("Please enter the list of number: ").split()))
selectionSort = SelectionSort(numbers)
selectionSort.selection_sort()
print(numbers)
