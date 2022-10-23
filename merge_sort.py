class MergeSort:
	@staticmethod
	def __merge(left_list, right_list):
		index = 0
		index2 = 0
		sorted_list = []
		
		while index < len(left_list) and index2 < len(right_list):
			if left_list[index] < right_list[index2]:
				sorted_list.append(left_list[index])
				index += 1
			else:
				sorted_list.append(right_list[index2])
				index2 += 1
				
		sorted_list += left_list[index: ]
		sorted_list += right_list[index2: ]
		return sorted_list
		
	def merge_sort(self, list):
		if len(list) < 2:
			return list
		else:
			mid = len(list) // 2
			left_list = self.merge_sort(list[: mid])
			right_list = self.merge_sort(list[mid: ])
			return self.__merge(left_list, right_list)
			
			
numbers = list(map(int, input("Please enter the list of number: ").split()))
mergeSort = MergeSort()
sorted_numbers =  mergeSort.merge_sort(numbers)
print(sorted_numbers)
