import random 
 
class TwoDList: 
    def __init__(self, numberOfRows, numberOfColumns): 
        self.numberOfRows = numberOfRows 
        self.numberOfColumns = numberOfColumns 
 
    def create_list(self): 
        self.arr = [[random.randint(0, 100) for _ in range(self.numberOfColumns)] for _ in range(self.numberOfRows)] 
        return self.arr 
         
    def sort_list(self, col_index): 
        self.arr = sorted(self.arr, key=lambda x: x[col_index]) 
        return self.arr
    # creating an object of the TwoDList class 
two_d_list = TwoDList(3, 4) 
 
# creating the 2-D list 
arr = two_d_list.create_list() 
print("Original 2-D List:") 
print(arr) 
 
# sorting the 2-D list based on the 2nd column 
sorted_arr = two_d_list.sort_list(1) 
print("Sorted 2-D List based on 2nd column:") 
print(sorted_arr)
