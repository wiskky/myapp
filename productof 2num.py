#THis program is multiplying the element in the list and print out the max no.
def max_of_product_num(nums):
	return ([a * b for a, b in zip(nums, nums[1:])])

my_list =  max_of_product_num([1,2,3,4,5,6])
print(max(my_list))