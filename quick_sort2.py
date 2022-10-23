class QuickSort:	
	def quick_sort(self, list):
		if len(list) < 2:
			return list
		else:
			mid = len(list) // 2
			pivot = list[mid]
			list.remove(list[mid])
			greater_than = []
			less_than = []
			
			for item in list:
				if item < pivot:
					less_than.append(item)
				else:
					greater_than.append(item)
					
			return self.quick_sort(less_than) + [pivot] + self.quick_sort(greater_than)
	
		
numbers = list(map(int, input("Please enter the list of number: ").split()))
quickSort = QuickSort()
sorted_numbers = quickSort.quick_sort(numbers)
print(sorted_numbers)	
