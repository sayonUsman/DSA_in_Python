class BubbleSort:
	def __init__(self, list):
		self.list = list
		
	def swap(self, index, index2):
		temp = self.list[index]
		self.list[index]= self.list[index2]
		self.list[index2] = temp
		
	def bubble_sort(self):
		for index in range(len(self.list) - 1):
			is_sorted = True
			for index2 in range(1, len(self.list) - index):
				if self.list[index2] < self.list[index2 - 1]:
					self.swap(index2 - 1, index2)
					is_sorted = False
			if is_sorted:
				return 


numbers = list(map(int, input("Please enter the list of number: ").split()))
bubbleSort = BubbleSort(numbers)
bubbleSort.bubble_sort()
print(numbers)
